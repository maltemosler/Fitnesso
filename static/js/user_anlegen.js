function nutzer_anlegen() {
    // get attributes from form
    const vorname = $("#register-vorname").val();
    const nachname = $("#register-nachname").val();

    const email = $("#register-email").val();
    const password = $("#register-password").val();
    const password_repeat = $("#register-password-repeat").val();

    // get boolean if validation of this things was successfully
    const validate_first_name = validateFirstName(vorname,  $("#register-error-vorname"));
    const validate_second_name = validateSecondName(nachname, $("#register-error-nachname"));
    const validate_email = validateEmail(email, $("#register-error-email"));
    const validate_password = validatePassword(password, password_repeat, $("#register-error-password"), $("#register-error-password-repeat"));

    // check if all validations were successfully
    if (validate_first_name && validate_second_name && validate_password && validate_email) {
        // send ajax request to webservers
        sendAJAX("register", {
                "vorname": vorname,
                "nachname": nachname,
                "email": email,
                "password": password
            },
            function () {
                // on success go back to the user verwaltung
                location.href="/user_verwaltung";
            }, function (status_code, message) {
                if(message === "409"){
                    // show error message that user already exists
                    $("#register-error-user_exist").show()
                }
            });
    }
}

