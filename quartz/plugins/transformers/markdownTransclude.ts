import { visit } from "unist-util-visit"
import path from "path"
import GithubSlugger from "github-slugger"
import { QuartzTransformerPlugin } from "../types"
import { FilePath, slugifyFilePath } from "../../util/path"

const MEDIA_EXTENSIONS = new Set([
  ".png",
  ".jpg",
  ".jpeg",
  ".gif",
  ".webp",
  ".svg",
  ".bmp",
  ".jxl",
  ".avif",
  ".pdf",
  ".mp4",
  ".webm",
  ".ogv",
  ".avi",
  ".mov",
  ".flv",
  ".wmv",
  ".mkv",
  ".mpg",
  ".mpeg",
  ".3gp",
  ".m4v",
  ".mp3",
  ".wav",
  ".m4a",
  ".ogg",
  ".oga",
  ".aac",
  ".flac",
])

const escapeHtml = (value: string): string =>
  value.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;")

function isExternal(url: string): boolean {
  return /^[a-z][a-z0-9+.-]*:/i.test(url) || url.startsWith("//") || url.startsWith("#")
}

export function isPageEmbed(url: string): boolean {
  if (!url || isExternal(url)) return false
  const target = url.split("#")[0]
  if (!target) return false
  return !MEDIA_EXTENSIONS.has(path.extname(target).toLowerCase())
}

function decode(value: string): string {
  try {
    return decodeURIComponent(value)
  } catch {
    return value
  }
}

/**
 * Turns a markdown image pointing at a note into a transclusion.
 *
 * In Markdown `![alt](note)` means "show an image", so Quartz renders a broken
 * `<img>` for note targets. `![[note]]` is the only wikilink form Quartz inlines,
 * and we do not want wikilinks, so this plugin rewrites the image node into the
 * `<blockquote class="transclude">` markup that `renderPage` already expands.
 */
export const MarkdownTransclude: QuartzTransformerPlugin = () => ({
  name: "MarkdownTransclude",
  markdownPlugins() {
    return [
      () => (tree: any) => {
        visit(tree, "image", (node: any, index: any, parent: any) => {
          if (!parent || index === undefined || index === null) return
          const url: string = node.url ?? ""
          if (!isPageEmbed(url)) return

          const [rawTarget, rawAnchor = ""] = url.split("#")
          const slug = slugifyFilePath(decode(rawTarget) as FilePath, true)
          if (!slug) return

          const anchor = decode(rawAnchor).trim()
          let block = ""
          if (anchor.length > 0) {
            block = anchor.startsWith("^") ? `#${anchor}` : `#${new GithubSlugger().slug(anchor)}`
          }

          const label = escapeHtml(node.alt && node.alt.length > 0 ? node.alt : slug)
          const blockAttribute = block ? ` data-block="${escapeHtml(block)}"` : ""

          parent.children[index] = {
            type: "html",
            value:
              `<blockquote class="transclude" data-url="${escapeHtml(slug)}"${blockAttribute}>` +
              `<a href="${escapeHtml(slug + block)}" class="transclude-inner">${label}</a>` +
              `</blockquote>`,
          }
        })
      },
    ]
  },
})
