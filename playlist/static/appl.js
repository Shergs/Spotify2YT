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
/*
function copyLink(){
  var copyText=document.getElementById("Recent_Playlists");
  copyText.select();
  copyText.setSelectionRange(0,99999);
  navigator.clipboard.writeText(copyText.value);
  alert("Copied the text: "+copyText.value);
}
*/