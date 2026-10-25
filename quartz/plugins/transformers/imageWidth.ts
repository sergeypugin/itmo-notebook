import { visit } from "unist-util-visit"
import { QuartzTransformerPlugin } from "../types"
import { isMediaUrl } from "./media"

function extractDimensions(source: string): { cleanSource: string; width: number | null; height: number | null } {
  const parts = source.split("|")
  if (parts.length < 2) {
    return { cleanSource: source, width: null, height: null }
  }

  const lastPart = parts[parts.length - 1]
  
  // Check for width x height format (e.g., 300x200)
  const whMatch = lastPart.match(/^(\d+)x(\d+)$/)
  if (whMatch) {
    const width = parseInt(whMatch[1], 10)
    const height = parseInt(whMatch[2], 10)
    if (!Number.isNaN(width) && width > 0 && !Number.isNaN(height) && height > 0) {
      return { cleanSource: parts.slice(0, -1).join("|"), width, height }
    }
  }
  
  // Check for just width
  const width = parseInt(lastPart, 10)
  if (!Number.isNaN(width) && width > 0) {
    return { cleanSource: parts.slice(0, -1).join("|"), width, height: null }
  }
  return { cleanSource: source, width: null, height: null }
}

const escapeHtml = (value: string): string =>
  value.replace(/&/g, "&").replace(/</g, "<").replace(/>/g, ">").replace(/"/g, "\"")

export const ImageWidth: QuartzTransformerPlugin = () => ({
  name: "ImageWidth",
  markdownPlugins() {
    return [
      () => (tree: any) => {
        visit(tree, "image", (node: any, index: any, parent: any) => {
          if (!parent || index === undefined || index === null) return
          const url: string = node.url ?? ""
          if (!isMediaUrl(url)) return

          // Check URL for dimensions (markdown images with |width in URL)
          const { cleanUrl, width: urlWidth, height: urlHeight } = extractDimensions(url)
          
          // Check alt for dimensions (markdown images with |width in alt, Obsidian-style)
          const alt: string = node.alt ?? ""
          const { cleanAlt, width: altWidth, height: altHeight } = extractDimensions(alt)
          
          const width = urlWidth ?? altWidth
          const height = urlHeight ?? altHeight
          const finalUrl = urlWidth ? cleanUrl : url
          const finalAlt = altWidth ? cleanAlt : alt
          
          if (!finalAlt) return
          
          if (width === null) return

          // Replace the image node with an HTML node that includes width and optionally height
          const escapedAlt = escapeHtml(finalAlt)
          const src = escapeHtml(finalUrl)
          const heightAttr = height ? ` height="${height}"` : ""

          parent.children[index] = {
            type: "html",
            value: `<img src="${src}" width="${width}"${heightAttr} alt="${escapedAlt}">`,
          }
        })
      },
    ]
  },
})