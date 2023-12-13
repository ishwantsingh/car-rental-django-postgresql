document.getElementById('forgotPasswordForm').addEventListener('submit', function(event){
    event.preventDefault(); // Prevent the default form submission

    var email = document.getElementById('email').value;

    // You would typically send an AJAX request to your server here
    // For demonstration, we'll just log to the console and show an alert
    console.log('Password Reset Email:', email);
    alert('If an account with that email address exists, a password reset link will be sent.');
});
