document.getElementById('signupForm').addEventListener('submit', function(event){
    event.preventDefault(); // Prevent the default form submission

    var fullName = document.getElementById('fullName').value;
    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;
    var confirmPassword = document.getElementById('confirmPassword').value;

    // Basic validation
    if(password !== confirmPassword){
        alert("Passwords do not match.");
        return;
    }

    console.log('Sign Up Details:', {
        fullName,
        email,
        password // Note: In a real application, you should not log passwords or send them in clear text.
    });

    // Here, you would usually send the data to a server
    // For demonstration purposes, we'll just show an alert
    alert('Sign Up Successful!');
});
