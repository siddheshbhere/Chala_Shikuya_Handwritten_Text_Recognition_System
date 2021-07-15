let switchCtn = document.querySelector("#switch-cnt");
let switchC1 = document.querySelector("#switch-c1");
let switchC2 = document.querySelector("#switch-c2");
let switchCircle = document.querySelectorAll(".switch__circle");
let switchBtn = document.querySelectorAll(".switch-btn");
let aContainer = document.querySelector("#a-container");
let bContainer = document.querySelector("#b-container");
let allButtons = document.querySelectorAll(".submit");

let getButtons = (e) => e.preventDefault()

let changeForm = (e) => {

    switchCtn.classList.add("is-gx");
    setTimeout(function(){
        switchCtn.classList.remove("is-gx");
    }, 1500)

    switchCtn.classList.toggle("is-txr");
    switchCircle[0].classList.toggle("is-txr");
    switchCircle[1].classList.toggle("is-txr");

    switchC1.classList.toggle("is-hidden");
    switchC2.classList.toggle("is-hidden");
    aContainer.classList.toggle("is-txl");
    bContainer.classList.toggle("is-txl");
    bContainer.classList.toggle("is-z200");
}

function validate(){
  var name = document.getElementById("name").value;
  var email = document.getElementById("email").value;
  var phone = document.getElementById("phone").value;
  var password = document.getElementById("password").value;
  var cpassword = document.getElementById("cpassword").value;
  var error_message = document.getElementById("error_message");

  error_message.style.padding = "10px";

  var text;
  if(name.length < 5){
    text = "Please Enter valid Username";
    error_message.innerHTML = text;
    return false;
  }
  if(email.indexOf("@") == -1 || email.length < 6){
    text = "Please Enter valid Email";
    error_message.innerHTML = text;
    return false;
  }
  if(isNaN(phone) || phone.length != 10){
    text = "Please Enter valid Phone Number";
    error_message.innerHTML = text;
    return false;
  }
  if(password.length < 8){
    text = "Please Enter Correct Password";
    error_message.innerHTML = text;
    return false;
  }
  if(cpassword.length <  8){
    text = "Please Enter Correct Password";
    error_message.innerHTML = text;
    return false;
  }
  if(cpassword != password)
  {
    text = "Confirm password is not equal to password";
    error_message.innerHTML = text;
    return false;
  }
  alert("Form Submitted Successfully!");
  return true;
}

function validatel(){
  var namel = document.getElementById("namel").value;
  var passwordl = document.getElementById("passwordl").value;
  var error_messagel = document.getElementById("error_messagel");
  var error_message1 = document.getElementById("error_message1");

  error_messagel.style.padding = "10px";
  error_message1.style.padding = "10px";

  var text;
  if(namel.length == 0){
    text = " Please Enter ";
    error_messagel.innerHTML = text;
    return false;
  }
  if(namel.length < 5){
    text = "Length must be greater than 5";
    error_messagel.innerHTML = text;
    return false;
  }
  if(namel.length > 20){
    text = "Length must be less than 20";
    error_messagel.innerHTML = text;
    return false;
  }
  if(passwordl.length == 0){
    text = "Please Enter";
    error_message1.innerHTML = text;
    return false;
  }
  if(passwordl.length < 8){
    text = "Length must be greater than 8";
    error_message1.innerHTML = text;
    return false;
  }
  if(passwordl.length > 20){
    text = "Length must be lesser than 20";
    error_message1.innerHTML = text;
    return false;
  }
  return true;
}



let mainF = (e) => {
    // for (var i = 0; i < allButtons.length; i++)
    //     allButtons[i].addEventListener("click", getButtons );
    for (var i = 0; i < switchBtn.length; i++)
        switchBtn[i].addEventListener("click", changeForm);

}

var rsubmit = document.getElementById("rsubmit").value;
var lsubmit = document.getElementById("lsubmit").value;

if (rsubmit) {
  let regi = (e) => {
      validate();
      window.addEventListener("submit", regi);

  }
} else {
  let logi = (e) => {
      validatel();
      window.addEventListener("submit", logi);

  }

}





window.addEventListener("load", mainF);
