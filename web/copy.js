// Adds a Copy button beside each paste-ready prompt block. The page works without it.
document.querySelectorAll("main pre").forEach((pre) => {
  if (!navigator.clipboard) return;
  let heading = pre.previousElementSibling;
  while (heading && !/^H[1-6]$/.test(heading.tagName)) heading = heading.previousElementSibling;
  const wrapper = document.createElement("div");
  wrapper.className = "prompt";
  pre.replaceWith(wrapper);
  const button = document.createElement("button");
  button.className = "copy";
  button.type = "button";
  button.textContent = "Copy";
  button.setAttribute("aria-label", "Copy " + (heading ? heading.textContent.trim() : "this block"));
  button.addEventListener("click", async () => {
    try {
      await navigator.clipboard.writeText(pre.innerText.trim());
      button.textContent = "Copied";
    } catch {
      const range = document.createRange();
      range.selectNodeContents(pre);
      getSelection().removeAllRanges();
      getSelection().addRange(range);
      button.textContent = "Selected";
    }
    setTimeout(() => (button.textContent = "Copy"), 2000);
  });
  wrapper.append(button, pre);
});
