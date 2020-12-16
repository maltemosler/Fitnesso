function nutzer_anlegen() {
    const vorname = $("#register-vorname").val();
    const nachname = $("#register-nachname").val();

    const email = $("#register-email").val();
    const password = $("#register-password").val();
    const password_repeat = $("#register-password-repeat").val();

    const validate_first_name = validateFirstName(vorname,  $("#register-error-vorname"));
    const validate_second_name = validateSecondName(nachname, $("#register-error-nachname"));
    const validate_email = validateEmail(email, $("#register-error-email"));
    const validate_password = validatePassword(password, password_repeat, $("#register-error-password"), $("#register-error-password-repeat"));

    if (validate_first_name && validate_second_name && validate_password && validate_email) {
        sendAJAX("register", {
                "vorname": vorname,
                "nachname": nachname,
                "email": email,
                "password": password
            },
            function () {
                console.log("register successfully");
                location.href="/";
            }, function (status_code, message) {
                if(message === "409"){
                    $("#register-error-user_exist").show()
                }
            });
    }
}