const navBtn = document.getElementById('nav-btn');
const cancelBtn = document.getElementById('cancel-btn');
const sideNav = document.getElementById('sidenav');
const modal = document.getElementById('modal');
const home = document.querySelectorAll('.home')

navBtn.addEventListener("click", function(){
    sideNav.classList.add('show');
    document.body.classList.add('no-scroll');
    modal.classList.add('showModal');
});

cancelBtn.addEventListener('click', function(){
    sideNav.classList.remove('show');
    modal.classList.remove('showModal');
    document.body.classList.remove('no-scroll');

});

home.forEach((btn) => {
    btn.addEventListener('click', () => {
        sideNav.classList.remove('show');
        document.body.classList.remove('no-scroll');
        modal.classList.remove('showModal');
    })
})

home.addEventListener('click', () => {
    sideNav.classList.remove('show');
    modal.classList.remove('showModal');
    document.body.classList.remove('no-scroll');

})

window.addEventListener('click', function(event){
    if(event.target === modal){
        sideNav.classList.remove('show');
        modal.classList.remove('showModal');
    }
});
