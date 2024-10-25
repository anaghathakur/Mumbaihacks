// Load login.html content dynamically into #content div
function loadLoginPage() {
    fetch("login.html")
        .then(response => response.text())
        .then(data => {
            document.getElementById("content").innerHTML = data;
            document.getElementById("loginModal").style.display = "block"; // Show modal
        })
        .catch(error => console.error("Error loading login page:", error));
}

// Close modal function
function closeModal() {
    document.getElementById("loginModal").style.display = "none";
}

// Show signup form and hide login form
function showSignupForm() {
    document.getElementById("loginForm").style.display = "none";
    document.getElementById("signupForm").style.display = "block";
}

// Show login form and hide signup form
function showLoginForm() {
    document.getElementById("signupForm").style.display = "none";
    document.getElementById("loginForm").style.display = "block";
}

// Optional: Close the modal when clicking outside it
window.onclick = function(event) {
    const modal = document.getElementById("loginModal");
    if (event.target == modal) {
        modal.style.display = "none";
    }
};
