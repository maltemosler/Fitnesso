function nutzer_anlegen() {
    const login_error = $("#register-error");

    const vorname = $("#register-vorname").val();
    const nachname = $("#register-nachname").val();

    const email = $("#register-email").val();
    const password = $("#register-password").val();

    const validate_email = validateEmail(email, login_error);
    const validate_password = validatePassword(password, password, login_error, login_error);

    if (validate_password && validate_email) {
        sendAJAX("register", {
                "vorname": vorname,
                "nachname": nachname,
                "email": email,
                "password": password,
            },
            function () {
                console.log("register successfully");
                location.href="/";
            }, function (status_code, message) {
                console.log(status_code);
                console.log(message);
            });
    }
}