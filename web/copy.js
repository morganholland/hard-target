// Adds a Copy button to each paste-ready prompt block. The page works without it.
document.querySelectorAll("pre").forEach((pre) => {
  if (!navigator.clipboard) return;
  const button = document.createElement("button");
  button.className = "copy";
  button.type = "button";
  button.textContent = "Copy";
  button.addEventListener("click", async () => {
    const text = pre.querySelector("code")?.innerText ?? pre.innerText;
    try {
      await navigator.clipboard.writeText(text.replace(/\n?Copy$/, ""));
      button.textContent = "Copied";
    } catch {
      button.textContent = "Select and copy";
    }
    setTimeout(() => (button.textContent = "Copy"), 2000);
  });
  pre.appendChild(button);
});
