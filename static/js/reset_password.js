function reset_password() {
    // get values from reset password
    const passwort = $("#reset-new_password").val();
    const password_repeat = $("#reset-new_password-confirmation").val();

    // validate the password
    const validate_password = validatePassword(passwort, password_repeat, $("#register-error-password"), $("#register-error-password-repeat"));
    if (validate_password) {
        // send ajax request to webserver
        sendAJAX("reset_password", {
                "user_id": getGETParams(),
                "new_password": passwort,
            },
            function () {
                // go back to user_verwaltung when successfully
                location.href = "/user_verwaltung";
            }, function (status_code, message) {
                // in case the server doesn't accept the server
                console.log(status_code);
                console.log(message);
            });
    }
}
