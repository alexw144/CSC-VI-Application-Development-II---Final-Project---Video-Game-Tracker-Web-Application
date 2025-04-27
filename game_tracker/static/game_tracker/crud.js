if (document.getElementById("profile-upd-submit-btn")){
    const profileUpdateSubmitButton = document.getElementById("profile-upd-submit-btn").addEventListener("click", profileUpdateSubmitButtonListener);
}

if (document.getElementById("game-stats-upd-submit-btn")){
    const gameUpdateSubmitButton = document.getElementById("game-stats-upd-submit-btn").addEventListener("click", gameStatUpdateSubmitButtonListener);
}

if (document.getElementById("user-review-submit-btn")){
    const userReviewSubmitButton = document.getElementById("user-review-submit-btn").addEventListener("click", userReviewSubmitButtonListener);
}

if (document.getElementById("comment-submit-btn")){
    const commentSubmitButton = document.getElementById("comment-submit-btn").addEventListener("click", commentSubmitButtonListener);
}

if (document.getElementById("post-submit-btn")){
    const postSubmitButton = document.getElementById("post-submit-btn").addEventListener("click", postSubmitButtonListener);
}

// asynchronous function with no arguements. Gets called when profile-upd-submit-btn is clicked.
async function profileUpdateSubmitButtonListener() {
    // Retvires the values of the html elements from the profile page that the user entered. This will be the new updated info.
    const fname = document.getElementById("f_name").value;
    const lname = document.getElementById("l_name").value;
    const bday = document.getElementById("bday").value;
    const gender = document.getElementById("gender").value;
    const email = document.getElementById("email").value;
    const usrn = document.getElementById("usrn").value;

    // Prepares the data to get sent to the server
    const data = {
        firstname: fname,
        lastname: lname,
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
        document.getElementById("current_name").textContent = "Name: " + data.firstname + " " + data.lastname;
        document.getElementById("current_usrn").textContent = "Username: " + data.username;
        document.getElementById("current_email").textContent = "Email Address: " + data.email;
        document.getElementById("current_bday").textContent = "Birthday: " + data.birthday;
        document.getElementById("current_gender").textContent = "Gender: " + data.gender;
    } else {
        alert('Error: Profile update could not be completed');
    }
};

// This function is for changing the time_played field from a duration to a float in hours.
document.addEventListener('DOMContentLoaded', function () {
    // Get the value from the input field
    const timePlayedElement = document.getElementById('time_played');
    
    // Check if the element exists
    if (timePlayedElement) {
        // Get the value from the input field
        const timePlayedInSeconds = parseFloat(timePlayedElement.value);

        // Convert the seconds to hours
        const timePlayedInHours = (timePlayedInSeconds / 3600).toFixed(2); // Convert and format to 2 decimal places

        // Update the input field with the new value in hours
        timePlayedElement.value = timePlayedInHours;
    } 
});

// asynchronous function with no arguements. Gets called when game-stats-upd-submit-btn is clicked.
async function gameStatUpdateSubmitButtonListener() {
    // Retvires the values of the html elements from the game detail page that the user entered. This will be the new updated info.
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
        action: 'update_user_game_stats', // tells view to update userstats
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

    // gets the games webpage slug for later use.
    const gameSlug = document.getElementById('gameSlug').textContent;

    // This sends the post request
    const response = await fetch(`/game/${gameSlug}/`, {method: 'POST', headers: {'Content-Type': 'application/json', 'X-CSRFToken': csrfToken}, body: JSON.stringify(data)});
    const result = await response.json();

    // If the request was successful, then it changes the html elements to the updated information. No page refresh is needed doing it this way.
    // It alerts the user if it succeeds or fails.
    if (result.status === 'success') {
        alert('Game stats updated successfully!');
        if (document.getElementById("current_user_game_stats_h3")) {
            document.getElementById("current_user_game_stats_h3").textContent = "Your Stats";
        }
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
        alert('Error: Game stats update could not be completed');
    }
};

// asynchronous function with no arguements. Gets called when user-review-submit-btn is clicked.
async function userReviewSubmitButtonListener() {
    // Retrieves the values of the html elements from the game detail page that the user entered. This will be the new review.
    const review_title = document.getElementById("review_title").value;
    const review_body = document.getElementById("review_body").value;

    // Prepares the data to get sent to the server
    const data = {
        action: 'submit_user_review', // tells view to update review
        title: review_title,
        review: review_body
    };
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    // gets the games webpage slug for later use.
    const gameSlug = document.getElementById('gameSlug').textContent;

    // This sends the post request
    const response = await fetch(`/game/${gameSlug}/`, {method: 'POST', headers: {'Content-Type': 'application/json', 'X-CSRFToken': csrfToken}, body: JSON.stringify(data)});
    const result = await response.json();

    // If the request was successful, then it changes the html elements to the updated information. No page refresh is needed doing it this way.
    // It alerts the user if it succeeds or fails.
    if (result.status === 'success') {
        alert('Review successfully posted!');
    } else {
        alert('Error: Review could not be completed');
    }
};

// asynchronous function. Gets called when comment-submit-btn is clicked.
async function commentSubmitButtonListener(postId) {
    // Retrieves the values of the html elements from the community page that the user entered. This will be the new created comment.
    const post_id = document.getElementById(`post_id_${postId}`).value;
    const post_comment = document.getElementById(`post_comment_${postId}`).value;

    // Prepares the data to get sent to the server
    const data = {
        action: 'create_user_comment', // tells view to update review
        post: post_id,
        comment: post_comment
    };
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    // This sends the post request
    const response = await fetch('/community/', {method: 'POST', headers: {'Content-Type': 'application/json', 'X-CSRFToken': csrfToken}, body: JSON.stringify(data)});
    const result = await response.json();

    // If the request was successful, then it changes the html elements to the updated information. No page refresh is needed doing it this way.
    // It alerts the user if it succeeds or fails.
    if (result.status === 'success') {
        alert('Comment posted successfully!');
        // This section of code adds the new comment to the community tab page. It creates, the whole html structure with the heading, date, and body.

        const commentDiv = document.createElement('div');

        const usernameHeader = document.createElement('h3');
        usernameHeader.textContent = result.comment.username;

        const dateCommentAdded = document.createElement('p');
        dateCommentAdded.textContent = result.comment.date_added;

        const commentBody = document.createElement('p');
        commentBody.textContent = result.comment.post_body;

        // Combine them
        commentDiv.appendChild(usernameHeader);
        commentDiv.appendChild(dateCommentAdded);
        commentDiv.appendChild(commentBody);

        // Insert into the page
        const commentSection = document.getElementById(`new-comments-section-${postId}`);
        commentSection.appendChild(commentDiv);
    } else {
        alert('Error: Comment could not be completed');
    }
};

// asynchronous function. Gets called when post-submit-btn is clicked.
async function postSubmitButtonListener() {
    // Retrieves the values of the html elements from the community page that the user entered. This will be the new created post.
    const post_game = document.getElementById("post_game").value;
    const post_title = document.getElementById("post_title").value;
    //const post_image = document.getElementById("post_image");  I could not get this to work in time :(
    const post_body = document.getElementById("post_body").value;
    const post_type = document.getElementById("post_type").value;

    // Prepares the data to get sent to the server
    const data = {
        action: 'create_user_post', // tells view to update review
        game: post_game,
        title: post_title,
        //image: post_image,
        body: post_body,
        type: post_type
    };
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    // This sends the post request
    const response = await fetch('/community/', {method: 'POST', headers: {'Content-Type': 'application/json', 'X-CSRFToken': csrfToken}, body: JSON.stringify(data)});
    const result = await response.json();

    // If the request was successful, then it changes the html elements to the updated information. No page refresh is needed doing it this way.
    // It alerts the user if it succeeds or fails.
    if (result.status === 'success') {
        alert('Post posted successfully!');
        // This section of code adds the new post to the community page.
        const postDiv = document.createElement('div');

        const postTitle = document.createElement('h2');
        postTitle.textContent = result.post.post_title;

        const postBody = document.createElement('p');
        postBody.textContent = result.post.post_body;

        //const postImage = document.createElement('img');
        //postImage.src = result.post.post_image;

        const postUser = document.createElement('p');
        postUser.textContent = "Posted by: " + result.post.post_user;
        
        const postGame = document.createElement('p');
        postGame.textContent = "Game: " + result.post.post_game;
        
        const postType = document.createElement('p');
        postType.textContent = "Post type: " + result.post.post_type;

        const postDate = document.createElement('p');
        postDate.textContent = "Upload date: " + result.post.post_date;

        // Combine them
        postDiv.appendChild(postTitle);
        postDiv.appendChild(postBody);
        //postDiv.appendChild(postImage);
        postDiv.appendChild(postUser);
        postDiv.appendChild(postGame);
        postDiv.appendChild(postType);
        postDiv.appendChild(postDate);

        // Insert into the page
        const newPost = document.getElementById('new-posts-section');
        newPost.appendChild(postDiv);
    } else {
        alert('Error: Post post could not be completed');
    }
};

// asynchronous function. Gets called when post-delete-btn is clicked. post_id is the {{ object.id }} from the html.
async function postDeleteButtonListener(post_id) {
    // Prepares the data to get sent to the server
    const data = {
        action: 'delete_user_post', // tells view to update review
        post: post_id
    };
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    // This sends the post request
    const response = await fetch('/community/', {method: 'POST', headers: {'Content-Type': 'application/json', 'X-CSRFToken': csrfToken}, body: JSON.stringify(data)});
    const result = await response.json();

    // If the request was successful, then it changes the html elements to the updated information. No page refresh is needed doing it this way.
    // It alerts the user if it succeeds or fails.
    if (result.status === 'success') {
        alert('Post deleted successfully!');
        // This section of code deletes the post to from community page.
        const postSection = document.getElementById(`post-section-${post_id}`);
        postSection.remove();
    } else {
        alert('Error: Post deletion could not be completed');
    }
};