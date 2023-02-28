const menu = document.querySelector('#mobile-menu');
const menuLinks = document.querySelector('.navbar__menu');

menu.addEventListener('click', function() {
  menu.classList.toggle('is-active');
  menuLinks.classList.toggle('active');
});
/*
document.querySelector('form').addEventListener('submit',function(event){
    let name=document.querySelector('#name').value;
    alert('Playlist is, '+name);
    event.preventDefault();

    console.log(name);

    

});*/
