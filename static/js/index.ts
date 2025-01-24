document.addEventListener("DOMContentLoaded", () => {
  const nameInput = document.getElementById("name-input") as HTMLInputElement;
  const greetButton = document.getElementById(
    "greet-button"
  ) as HTMLButtonElement;

  greetButton.addEventListener("click", () => {
    if (!nameInput) return;

    if (nameInput.value === "") {
      alert("Please enter a name");
      return;
    }

    greet(nameInput.value);
  });
});

function greet(name: string) {
  fetch(`/greet/${name}`)
    .then((response) => response.text())
    .then((data) => {
      alert(data);
    });
}
