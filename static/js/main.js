// JavaScript to toggle navbar on smaller screens
document.addEventListener('DOMContentLoaded', function() {
    const navToggler = document.querySelector('.navbar-toggler');
    const navMenu = document.querySelector('#navbarNav');

    navToggler.addEventListener('click', function() {
        navMenu.classList.toggle('show');
    });
});

// Smooth scrolling for internal links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});
