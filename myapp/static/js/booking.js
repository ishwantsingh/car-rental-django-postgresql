document.getElementById('bookingForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the form from submitting the traditional way

    // Perform your validation and booking logic here
    var fromDate = document.getElementById('fromDate').value;
    var toDate = document.getElementById('toDate').value;
    var pickupLocation = document.getElementById('pickupLocation').value;
    var dropoffLocation = document.getElementById('dropoffLocation').value;
    var couponCode = document.getElementById('couponCode').value;

    // For demonstration, we'll just log the values to the console
    console.log('Booking Details:', {
        fromDate,
        toDate,
        pickupLocation,
        dropoffLocation,
        couponCode
    });

    // You would typically send this data to a server here
    // ...

    alert('Form submitted! Check the console for the booking details.');
});
