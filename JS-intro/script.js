// Change text content dynamically
document.getElementById("changeTextButton").addEventListener("click", function() {
  document.getElementById("text").textContent = "The text has been changed!";
});

// Modify CSS styles dynamically
document.getElementById("changeStyleButton").addEventListener("click", function() {
  const styleText = document.getElementById("styleText");
  styleText.style.color = styleText.style.color === "red" ? "black" : "red";
});

// Add or remove an element dynamically
document.getElementById("toggleButton").addEventListener("click", function() {
  const elementContainer = document.getElementById("elementContainer");
  
  // Check if the paragraph already exists
  const existingParagraph = document.getElementById("dynamicParagraph");
  
  if (existingParagraph) {
    // If the paragraph exists, remove it
    elementContainer.removeChild(existingParagraph);
  } else {
    // If the paragraph doesn't exist, create it
    const newParagraph = document.createElement("p");
    newParagraph.id = "dynamicParagraph";
    newParagraph.textContent = "This is a dynamically added paragraph!";
    elementContainer.appendChild(newParagraph);
  }
});
