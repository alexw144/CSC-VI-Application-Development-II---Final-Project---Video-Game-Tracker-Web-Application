const profileUpdateSubmitButton = document.getElementById("profile-upd-submit-btn").addEventListener("click", profileUpdateSubmitButtonListener);

// asynchronous function with no arguements. Gets called when profile-upd-submit-btn is clicked.
async function profileUpdateSubmitButtonListener() {

    const bday = document.getElementById("bday").value;
    const gender = document.getElementById("gender").value;
    const email = document.getElementById("email").value;
    const usrn = document.getElementById("usrn").value;

    const data = {
        birthday: bday,
        gender: gender,
        email: email,
        username: usrn
    };
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    const response = await fetch('/profile/${usrn}/', {method: 'POST', headers: {'Content-Type': 'application/json', 'X-CSRFToken': csrfToken}, body: JSON.stringify(data)});
    const result = await response.json();
    console.log(result);

    if (result.status === 'success') {
        alert('Profile updated successfully!');
        document.getElementById("profile_page_heading").textContent = data.username + "'s Profile";
        document.getElementById("current_usrn").textContent = "Username: " + data.username;
        document.getElementById("current_email").textContent = "Email Address: " + data.email;
        document.getElementById("current_bday").textContent = "Birthday: " + data.birthday;
        document.getElementById("current_gender").textContent = "Gender: " + data.gender;
    } else {
        alert('Error: Profile update could not be completed');
    }
};
