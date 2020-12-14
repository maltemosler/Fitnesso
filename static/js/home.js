

function hauptziel_erstellen() {
    const ziel = $("#home-hauptziel").val();

    sendAJAX("hauptziel_erstellen", {
            "ziel": ziel,
        },
        function () {
            location.reload();
        }, function (status_code, message) {
            console.log(status_code);
            console.log(message);
        });
}


function login() {
    const login_error = $("#login-error");

    const email = $("#login-email").val();
    const password = $("#login-password").val();

    const validate_email = validateEmail(email, login_error);
    const validate_password = validatePassword(password, password, login_error, login_error);

    if (validate_password && validate_email) {
        sendAJAX("user_login", {
                "email": email,
                "password": password,
            },
            function () {
                console.log("logged in");
                sessionStorage.setItem('status', 'loggedIn');
                location.reload();
            }, function (status_code, message) {
                console.log("tjgwerz");
                console.log(status_code);
                console.log(message);

            });
    }
}

function delete_user(user_id) {

    sendAJAX("delete_user", {
            "user_id": user_id,
        },
        function () {
            location.reload();
        }, function (status_code, message) {
            console.log(status_code);
            console.log(message);

        });

}
