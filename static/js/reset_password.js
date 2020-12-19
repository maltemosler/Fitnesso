function reset_password() {
    const passwort = $("#reset-new_password").val();
    const password_repeat = $("#reset-new_password-confirmation").val();

    const validate_password = validatePassword(passwort, password_repeat, $("#register-error-password"), $("#register-error-password-repeat"));
    if (validate_password) {
        sendAJAX("reset_passwort", {
                "user_id": getGETParams(),
                "new_password": passwort,
            },
            function () {
                location.href = "/user_verwaltung";
            }, function (status_code, message) {
                console.log(status_code);
                console.log(message);
            });
    }
}
