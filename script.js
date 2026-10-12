```javascript
document.addEventListener("DOMContentLoaded", () => {
    const statusElement = document.getElementById("status");
    const yearElement = document.getElementById("year");

    // Display website status
    if (statusElement) {
        statusElement.textContent = "Website loaded successfully";
        statusElement.setAttribute("role", "status");
    }

    // Display the current year in the footer
    if (yearElement) {
        yearElement.textContent = new Date().getFullYear();
    }
});
