export const MEDIA_EXTENSIONS = new Set([
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

export function isMediaUrl(url: string): boolean {
  if (!url) return false
  const target = url.split("#")[0].split("|")[0] // remove anchor and width
  if (!target) return false
  return MEDIA_EXTENSIONS.has(target.slice(target.lastIndexOf(".")).toLowerCase())
}