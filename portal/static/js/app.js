var login = document.querySelector('#login')
var studentSignUp = document.querySelector('#student-signup')
var closeBtn = document.querySelector('.close-btn')
closeBtn.addEventListener('click', close)


function signUp() {
    login.style.display = "none"
    studentSignUp.style.display = "block"
}

function close() {
    login.style.display = "block"
    studentSignUp.style.display = "none"
}