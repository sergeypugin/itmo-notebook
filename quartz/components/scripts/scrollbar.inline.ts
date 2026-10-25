const inlineSelector = ".katex:not(.katex-display > .katex)"
let mutationObserver: MutationObserver | undefined
let frame = 0

function scheduleSync() {
  if (frame) return
  frame = requestAnimationFrame(sync)
}

function sync() {
  frame = 0
  mutationObserver?.disconnect()

  const article = document.querySelector("article")
  if (!article) return

  article.querySelectorAll<HTMLElement>(inlineSelector).forEach((element) => {
    const parent = element.parentElement?.closest("p, li, td, th, blockquote, div")
    const availableWidth = parent?.clientWidth ?? element.clientWidth
    element.classList.toggle("horizontal-scroll-inline", element.scrollWidth > availableWidth + 1)
  })

  mutationObserver = new MutationObserver((records) => {
    if (
      records.some(
        ({ target, type }) =>
          type === "childList" ||
          (type === "attributes" && target instanceof HTMLElement && target.matches(".callout")),
      )
    ) {
      scheduleSync()
    }
  })
  mutationObserver.observe(article, {
    childList: true,
    subtree: true,
    attributes: true,
    attributeFilter: ["class"],
  })
}

document.addEventListener("nav", scheduleSync)
document.addEventListener("transitionend", (event) => {
  if (event.target instanceof HTMLElement && event.target.matches(".callout")) scheduleSync()
})
window.addEventListener("resize", scheduleSync)
document.addEventListener("load", scheduleSync, true)
document.fonts?.ready.then(scheduleSync)
scheduleSync()
