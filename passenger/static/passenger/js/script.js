let navebar = document.querySelector('.header .navbar');

document.querySelector('#menu-bar').onclick = () => {
    navebar.classList.toggle('.active');
}

window.onscroll = () => {
    navebar.classList.remove('active');
}