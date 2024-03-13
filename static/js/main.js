// main.js

document.getElementById('vendor-form').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission behavior

    // Get form data
    var formData = new FormData(this); // 'this' refers to the form element itself

    // Send form data to Django backend using Fetch API
    fetch('/submit/', {
        method: 'POST',
        body: formData,
    })
    .then(response => {
        if (response.ok) {
            // If form submission is successful, do something (e.g., display success message)
            console.log('Form submitted successfully!');
            alert('Vendor application submitted successfully!');
            document.getElementById('vendor-form').reset(); // Clear form fields
        } else {
            // If there's an error, handle it (e.g., display error message)
            console.error('Form submission failed:', response.statusText);
            alert('Failed to submit vendor application. Please try again.');
        }
    })
    .catch(error => {
        // Handle network errors
        console.error('Error:', error);
        alert('An error occurred while submitting the vendor application.');
    });
});
