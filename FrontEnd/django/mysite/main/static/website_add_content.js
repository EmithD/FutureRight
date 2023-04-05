const checkbox = document.getElementById("checkbox");
const startTestButton = document.getElementById("review-button");

startTestButton.addEventListener("click", function(event) {
  if (!checkbox.checked) {
    event.preventDefault();
    checkbox.setCustomValidity("Please agree to the Terms and Conditions.");
    checkbox.reportValidity();
  } else {
    checkbox.setCustomValidity("");
  }
});