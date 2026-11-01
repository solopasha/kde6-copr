document.querySelectorAll(".copy-button").forEach((button) => {
  button.addEventListener("click", async () => {
    const command = document.getElementById(button.dataset.copyTarget).textContent;
    try {
      await navigator.clipboard.writeText(command);
      button.classList.add("copied");
      button.setAttribute("aria-label", "Commands copied");
    } catch {
      button.setAttribute("aria-label", "Unable to copy commands");
    }
    window.setTimeout(() => {
      button.classList.remove("copied");
      button.setAttribute("aria-label", "Copy commands");
    }, 2000);
  });
});
