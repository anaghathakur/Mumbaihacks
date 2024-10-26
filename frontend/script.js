// Show the modal
function loadLoginPage() {
    document.getElementById("loginModal").style.display = "block";
}

// Close the modal
function closeModal() {
    document.getElementById("loginModal").style.display = "none";
}

// Switch to the signup form
function showSignupForm() {
    document.getElementById("loginForm").style.display = "none";
    document.getElementById("signupForm").style.display = "block";
}

// Switch to the login form
function showLoginForm() {
    document.getElementById("signupForm").style.display = "none";
    document.getElementById("loginForm").style.display = "block";
}

function handleDashboardSubmit(event) {
    event.preventDefault();

    // Collect user data
    const userData = {
        name: document.getElementById("name").value,
        dob: document.getElementById("dob").value,
        income: document.getElementById("income").value,
        employment: document.getElementById("employment").value,
        occupation: document.getElementById("occupation").value,
        education: document.getElementById("education").value,
        homeOwnership: document.getElementById("homeOwnership").value,
        mobile: document.getElementById("mobile").value,
        address: document.getElementById("address").value,
        maritalStatus: document.getElementById("maritalStatus").value,
        children: document.getElementById("children").value,
        liquidity: document.getElementById("liquidity").value,
    };

    // Save data to local storage
    localStorage.setItem("userData", JSON.stringify(userData));

    // Show success message or redirect
    alert("Your information has been saved successfully!");
}

function displayUserInfo() {
    const storedData = JSON.parse(localStorage.getItem("userData"));
    if (storedData) {
        document.getElementById("name").value = storedData.name;
        document.getElementById("dob").value = storedData.dob;
        document.getElementById("income").value = storedData.income;
        document.getElementById("employment").value = storedData.employment;
        document.getElementById("occupation").value = storedData.occupation;
        document.getElementById("education").value = storedData.education;
        document.getElementById("homeOwnership").value = storedData.homeOwnership;
        document.getElementById("mobile").value = storedData.mobile;
        document.getElementById("address").value = storedData.address;
        document.getElementById("maritalStatus").value = storedData.maritalStatus;
        document.getElementById("children").value = storedData.children;
        document.getElementById("liquidity").value = storedData.liquidity;
    }
}

// Call displayUserInfo on page load
document.addEventListener("DOMContentLoaded", displayUserInfo);

// redirection 
// script.js
function handleDashboardSubmit(event) {
    event.preventDefault();
    
    // Get form data
    const name = document.getElementById("name").value;
    const dob = document.getElementById("dob").value;
    const income = document.getElementById("income").value;
    const employment = document.getElementById("employment").value;
    const occupation = document.getElementById("occupation").value;
    const education = document.getElementById("education").value;
    const homeOwnership = document.getElementById("homeOwnership").value;
    const mobile = document.getElementById("mobile").value;
    const address = document.getElementById("address").value;
    const maritalStatus = document.getElementById("maritalStatus").value;
    const children = document.getElementById("children").value;
    const liquidity = document.getElementById("liquidity").value;

    // Save data to localStorage
    localStorage.setItem("name", name);
    localStorage.setItem("dob", dob);
    localStorage.setItem("income", income);
    localStorage.setItem("employment", employment);
    localStorage.setItem("occupation", occupation);
    localStorage.setItem("education", education);
    localStorage.setItem("homeOwnership", homeOwnership);
    localStorage.setItem("mobile", mobile);
    localStorage.setItem("address", address);
    localStorage.setItem("maritalStatus", maritalStatus);
    localStorage.setItem("children", children);
    localStorage.setItem("liquidity", liquidity);

    // Redirect to the Student Dashboard
    window.location.href = "userdashboard.html";
}
