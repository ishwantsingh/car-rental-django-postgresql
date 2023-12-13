document.addEventListener('DOMContentLoaded', function() {
  const userLoginBtn = document.querySelector('.role-selection .role-button:first-child');
  const adminLoginBtn = document.querySelector('.role-selection .role-button:last-child');

  userLoginBtn.addEventListener('click', function() {
    console.log("User Login Clicked");
    userLoginBtn.classList.add('active');
    adminLoginBtn.classList.remove('active');
    // Implement logic for User login here...
  });

  adminLoginBtn.addEventListener('click', function() {
    console.log("Admin Login Clicked");
    adminLoginBtn.classList.add('active');
    userLoginBtn.classList.remove('active');
    // Implement logic for Admin login here...
  });
});

function submitForm(event) {
  event.preventDefault();
  // Implement form submission logic here...
}

// Rest of your JavaScript code...
