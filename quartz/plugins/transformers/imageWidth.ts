import { visit } from "unist-util-visit"
import { QuartzTransformerPlugin } from "../types"
import { isMediaUrl } from "./media"

export interface ImageDimensions {
  /** Alt text with the size suffix removed. */
  alt: string
  width: number | null
  height: number | null
}

const WIDTH_AND_HEIGHT = /^(\d+)(?:x(\d+))?$/
const HEIGHT_ONLY = /^x(\d+)$/

function parseSize(value: string): Omit<ImageDimensions, "alt"> | null {
  const both = WIDTH_AND_HEIGHT.exec(value)
  if (both) {
    const width = Number(both[1])
    const height = both[2] === undefined ? null : Number(both[2])
    if (width <= 0 || (height !== null && height <= 0)) return null
    return { width, height }
  }

  const onlyHeight = HEIGHT_ONLY.exec(value)
  if (onlyHeight) {
    const height = Number(onlyHeight[1])
    return height > 0 ? { width: null, height } : null
  }

  return null
}

/**
 * Reads an Obsidian-style size suffix from image alt text, e.g. `pic.png|200`,
 * `pic.png|200x150` or `pic.png|x150`. The segment after the last `|` is either
 * a size or an alias; only a valid size is stripped. Alt text without `|` is
 * never a size, so a bare `200` stays the alt text.
 */
export function extractDimensions(alt: string): ImageDimensions {
  const separator = alt.lastIndexOf("|")
  if (separator === -1) return { alt, width: null, height: null }

  const size = parseSize(alt.slice(separator + 1))
  if (!size) return { alt, width: null, height: null }

  return { alt: alt.slice(0, separator), ...size }
}

const escapeHtml = (value: string): string =>
  value
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;")

export const ImageWidth: QuartzTransformerPlugin = () => ({
  name: "ImageWidth",
  markdownPlugins() {
    return [
      () => (tree: any) => {
        visit(tree, "image", (node: any, index: any, parent: any) => {
          if (!parent || index === undefined || index === null) return
          const url: string = node.url ?? ""
          if (!isMediaUrl(url)) return

          const { alt, width, height } = extractDimensions(node.alt ?? "")
          if (width === null && height === null) return

          const attributes = [
            `src="${escapeHtml(url)}"`,
            width === null ? null : `width="${width}"`,
            height === null ? null : `height="${height}"`,
            `alt="${escapeHtml(alt)}"`,
          ].filter((attribute): attribute is string => attribute !== null)

          parent.children[index] = {
            type: "html",
            value: `<img ${attributes.join(" ")}>`,
          }
        })
      },
    ]
  },
})
