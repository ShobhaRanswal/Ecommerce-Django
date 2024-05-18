$(document).ready(function() {
    var currentIndex = 0;
    var images = $('.album-image');
    var totalImages = images.length;

    function showNextImage() {
        images.eq(currentIndex).animate({opacity: 0}, 1000);
        currentIndex = (currentIndex + 1) % totalImages;
        images.eq(currentIndex).animate({opacity: 1}, 1000);
    }

    setInterval(showNextImage, 5000); // Change image every 5 seconds
});
