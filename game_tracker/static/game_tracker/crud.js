const profileUpdateSubmitButton = document.getElementById("profile-upd-submit-btn").addEventListener("click", profileUpdateSubmitButtonListener);

// asynchronous function with no arguements. Gets called when profile-upd-submit-btn is clicked.
async function profileUpdateSubmitButtonListener() {
    // Retvires the values of the html elements from the profile page that the user entered. This will be the new updated info.
    const bday = document.getElementById("bday").value;
    const gender = document.getElementById("gender").value;
    const email = document.getElementById("email").value;
    const usrn = document.getElementById("usrn").value;

    // Prepares the data to get sent to the server
    const data = {
        birthday: bday,
        gender: gender,
        email: email,
        username: usrn
    };
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    // This send the post request
    const response = await fetch('/profile/${usrn}/', {method: 'POST', headers: {'Content-Type': 'application/json', 'X-CSRFToken': csrfToken}, body: JSON.stringify(data)});
    const result = await response.json();

    // If the request was successful, then it changes the html elements to the updated information. No page refresh is needed doing it this way.
    // It alerts the user if it succeeds or fails.
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
