if (document.getElementById("profile-upd-submit-btn")){
    const profileUpdateSubmitButton = document.getElementById("profile-upd-submit-btn").addEventListener("click", profileUpdateSubmitButtonListener);
}

if (document.getElementById("game-stats-upd-submit-btn")){
    const gameUpdateSubmitButton = document.getElementById("game-stats-upd-submit-btn").addEventListener("click", gameStatUpdateSubmitButtonListener);
}

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

    // This sends the post request
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

document.addEventListener('DOMContentLoaded', function () {
    // Get the value from the input field
    const timePlayedInSeconds = parseFloat(document.getElementById('time_played').value);

    // Convert the seconds to hours
    const timePlayedInHours = (timePlayedInSeconds / 3600).toFixed(2); // Convert and format to 2 decimal places

    // Update the input field with the new value in hours
    document.getElementById('time_played').value = timePlayedInHours;
});

// asynchronous function with no arguements. Gets called when game-stats-upd-submit-btn is clicked.
async function gameStatUpdateSubmitButtonListener() {
    // Retvires the values of the html elements from the profile page that the user entered. This will be the new updated info.
    const time_played = parseFloat(document.getElementById("time_played").value);
    const first_played = document.getElementById("first_played").value;
    const last_played = document.getElementById("last_played").value;
    const date_beaten = document.getElementById("date_beaten").value;
    const status = document.getElementById("status").value;
    const rating = document.getElementById("rating").value;
    const perc_comp = document.getElementById("perc_comp").value;
    const ach_count = document.getElementById("ach_count").value;
    const notes = document.getElementById("notes").value;

    // Prepares the data to get sent to the server
    const data = {
        time: time_played,
        first: first_played,
        last: last_played,
        beaten: date_beaten,
        status: status,
        rating: rating,
        percent: perc_comp,
        achievements: ach_count,
        notes: notes
    };
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    const gameSlug = document.getElementById('gameSlug').textContent;

    // This sends the post request
    const response = await fetch(`/game/${gameSlug}/`, {method: 'POST', headers: {'Content-Type': 'application/json', 'X-CSRFToken': csrfToken}, body: JSON.stringify(data)});
    const result = await response.json();

    // If the request was successful, then it changes the html elements to the updated information. No page refresh is needed doing it this way.
    // It alerts the user if it succeeds or fails.
    if (result.status === 'success') {
        alert('Profile updated successfully!');
        document.getElementById("current_user_game_stats_h3").textContent = "Your Stats";
        document.getElementById("current_time_played").textContent = "Time Played: " + data.time;
        document.getElementById("current_first_played").textContent = "First Played: " + data.first;
        document.getElementById("current_last_played").textContent = "Last Played: " + data.last;
        document.getElementById("current_date_beaten").textContent = "Date Beaten: " + data.beaten;
        document.getElementById("current_status").textContent = "Status: " + data.status;
        document.getElementById("current_rating").textContent = "Rating: " + data.rating;
        document.getElementById("current_percent_completed").textContent = "Percent Completed: " + data.percent;
        document.getElementById("current_achievement_count").textContent = "Achievement Count: " + data.achievements;
        document.getElementById("current_notes").textContent = "Notes: " + data.notes;
    } else {
        alert('Error: Profile update could not be completed');
    }
};
