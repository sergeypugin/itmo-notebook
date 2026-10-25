import { test, describe } from "node:test"
import assert from "node:assert/strict"
import { unified } from "unified"
import remarkParse from "remark-parse"
import { extractDimensions, ImageWidth } from "./imageWidth"
import { BuildCtx } from "../../util/ctx"

function parse(markdown: string): any {
  const ctx = {} as BuildCtx
  const processor = unified().use(remarkParse).use(ImageWidth().markdownPlugins!(ctx))
  return processor.runSync(processor.parse(markdown))
}

function firstChild(markdown: string): any {
  return parse(markdown).children[0].children[0]
}

describe("extractDimensions", () => {
  test("width only", () => {
    assert.deepEqual(extractDimensions("pic.png|200"), { alt: "pic.png", width: 200, height: null })
  })

  test("width and height", () => {
    assert.deepEqual(extractDimensions("pic.png|200x150"), {
      alt: "pic.png",
      width: 200,
      height: 150,
    })
  })

  test("height only", () => {
    assert.deepEqual(extractDimensions("pic.png|x150"), {
      alt: "pic.png",
      width: null,
      height: 150,
    })
  })

  test("keeps a bare number as alt text", () => {
    assert.deepEqual(extractDimensions("200"), { alt: "200", width: null, height: null })
  })

  for (const invalid of ["abc", "0", "-5", "200x", "x", ""]) {
    test(`rejects "${invalid}"`, () => {
      assert.deepEqual(extractDimensions(`pic.png|${invalid}`), {
        alt: `pic.png|${invalid}`,
        width: null,
        height: null,
      })
    })
  }
})

describe("ImageWidth", () => {
  test("applies width from alt and strips the suffix", () => {
    const node = firstChild("![pic.png|200](a/pic.png)")
    assert.equal(node.type, "html")
    assert.match(node.value, /src="a\/pic\.png"/)
    assert.match(node.value, /width="200"/)
    assert.match(node.value, /alt="pic\.png"/)
    assert.doesNotMatch(node.value, /height=/)
  })

  test("applies width and height", () => {
    const node = firstChild("![pic.png|200x150](a/pic.png)")
    assert.equal(node.type, "html")
    assert.match(node.value, /width="200"/)
    assert.match(node.value, /height="150"/)
    assert.match(node.value, /alt="pic\.png"/)
  })

  test("applies height only", () => {
    const node = firstChild("![pic.png|x150](a/pic.png)")
    assert.equal(node.type, "html")
    assert.match(node.value, /height="150"/)
    assert.doesNotMatch(node.value, /width=/)
    assert.match(node.value, /alt="pic\.png"/)
  })

  test("leaves images without a size untouched", () => {
    const node = firstChild("![pic.png](a/pic.png)")
    assert.equal(node.type, "image")
    assert.equal(node.alt, "pic.png")
    assert.equal(node.url, "a/pic.png")
  })

  test("leaves non-media targets untouched", () => {
    const node = firstChild("![pic.png|200](a/note)")
    assert.equal(node.type, "image")
    assert.equal(node.alt, "pic.png|200")
    assert.equal(node.url, "a/note")
  })

  test("takes the size from alt and keeps the url intact", () => {
    const node = firstChild("![pic.png|200](a/pic.png|200)")
    assert.equal(node.type, "html")
    assert.match(node.value, /src="a\/pic\.png\|200"/)
    assert.match(node.value, /width="200"/)
    assert.match(node.value, /alt="pic\.png"/)
  })

  test("escapes alt text", () => {
    const node = firstChild('![a"b.png|200](x/a.png)')
    assert.equal(node.type, "html")
    assert.match(node.value, /alt="a&quot;b\.png"/)
  })
})
