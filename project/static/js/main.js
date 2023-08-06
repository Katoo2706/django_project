document.addEventListener('DOMContentLoaded', function() {
    const date = new Date();
    const yearElement = document.querySelector('.year');

    if (yearElement) {
        yearElement.innerHTML = date.getFullYear();
    }
});


setTimeout(function () {
    $('#message').fadeOut('slow'); // Use .message for a class or #message for an ID
}, 3000);
