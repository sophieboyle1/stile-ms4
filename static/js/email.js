// --- Immediately invoked function for email.js ---
(function(){emailjs.init("user_qI0f2g6tNqj3cj8yeKtiz");})();

// --- Sends e-mail to my e-mail adress
document.getElementById('contactForm').addEventListener('submit', function (event) {
    event.preventDefault();
    emailjs.send("gmail", "contact", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "contact_request": contactForm.projectsummary.value
    })
        .then(
            function success() {
                notification();
                setTimeout(refresh, 2500);
            },
            function failure() {
                failToSend();
            }
        );
    return false;
});

// --- Changes text in button to notify user that e-mail was sent successfuly (200) ---
function notification() {
    $("#submit").text("E-mail submitted!");
}

// --- Refreshes form ONLY ---
function refresh() {
    $("#submit").text("Submit");
    document.getElementById("contactForm").reset();
}

// --- E-mail failed to sent (404) ---
function failToSend(){
    $("#submit").text("Failed to submit. Refresh page");
}


