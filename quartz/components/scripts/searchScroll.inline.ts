function initSearchPreviewScrollFix() {
  const searchContainer = document.querySelector(".search-container")
  if (!searchContainer) return

  const adjustScroll = () => {
    const preview = searchContainer.querySelector(".preview-container")
    if (!preview) return

    const highlights = Array.from(preview.getElementsByClassName("highlight"))
    if (highlights.length === 0) {
      preview.scrollTop = 0
      return
    }

    let minTop = Infinity
    for (const el of highlights) {
      let offset = 0
      let curr: HTMLElement | null = el as HTMLElement
      while (curr && curr !== preview) {
        offset += curr.offsetTop
        curr = curr.offsetParent as HTMLElement | null
      }
      if (offset < minTop) {
        minTop = offset
      }
    }

    preview.scrollTop = Math.max(0, minTop - 120)
  }

  const observer = new MutationObserver(() => {
    requestAnimationFrame(() => {
      adjustScroll()
      setTimeout(adjustScroll, 20)
      setTimeout(adjustScroll, 100)
      setTimeout(adjustScroll, 300)
    })
  })

  observer.observe(searchContainer, { childList: true, subtree: true })
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initSearchPreviewScrollFix)
} else {
  initSearchPreviewScrollFix()
}
document.addEventListener("nav", initSearchPreviewScrollFix)
