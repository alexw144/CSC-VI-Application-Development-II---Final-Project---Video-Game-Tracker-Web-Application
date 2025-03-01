const bday = document.getElementById("bday").value;
const gender = document.getElementById("gender").value;
const email = document.getElementById("email").value;
const usrn = document.getElementById("usrn").value;
const profileUpdateSubmitButton = document.getElementById("profile-upd-submit-btn").addEventListener("click", profileUpdateSubmitButtonListener);

// asynchronous function with no arguements. Gets called when submit-btn is clicked.
async function profileUpdateSubmitButtonListener() {

    const data = {
        birthday: bday,
        gender: gender,
        email: email,
        username: usrn
    };

    const postRequest = await fetch('/Profile/');

};