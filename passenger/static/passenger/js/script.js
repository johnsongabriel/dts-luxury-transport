let navebar = document.querySelector('.header .navbar');

document.querySelector('#menu-btn').onclick = () =>{
    navebar.classList.toggle('active');
}

window.onscroll = () => {
    navebar.classList.remove('active');
}