const navBtn = document.getElementById('nav-btn');
const mobileMenu = document.getElementById('mobile-menu');
const elementToRemove = document.getElementById('movingElementExample');

console.log("Hello")

navBtn.addEventListener('click', () => {
    console.log("Clicked")
    setTimeout(() => {
        mobileMenu.classList.toggle('hidden');
    }, 400);
});


