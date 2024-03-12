const menuToggle = document.querySelector('.toggle');
const showcase = document.querySelector('.showcase');
const loginRegisterLink = document.querySelector('.menu ul li:nth-child(3) a');

menuToggle.addEventListener('click', () => {
  menuToggle.classList.toggle('active');
  showcase.classList.toggle('active');
});

function tweetShare() {
  window.open('https://twitter.com/intent/tweet?text=Check%20out%20this%20awesome%20website%21%20https%3A%2F%2Fexample.com%2F');
}
  
function shareOnFacebook() {
    var url = encodeURIComponent(window.location.href);
    window.open('https://www.facebook.com/sharer/sharer.php?u=' + url, '_blank');
}

function openForm(formName) {
  document.getElementById(formName).style.display = "block";

}

function closeForm(loginForm) {
  document.getElementById(loginForm).style.display = "none";
}

function openRegisterForm() {
  // Close the login form if it's open
  closeForm("loginForm");
  // Open the register form
  openForm("registerForm");
}

function closeRegisterForm() {
  // Close the register form
  closeForm("registerForm");
}
