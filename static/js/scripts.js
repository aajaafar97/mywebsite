window.onload = function() {
    var contactLink = document.querySelector('nav a:last-child');
    contactLink.addEventListener('click', function(event) {
        event.preventDefault();
        alert('Contact me at: aajaafar@umich.edu');
    });
}
