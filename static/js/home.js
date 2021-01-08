function login() {
    const login_error = $("#login-error-text");

    // get content from email and password field
    const email = $("#login-email").val();
    const password = $("#login-password").val();

    const validate_email = validateEmail(email, login_error);

    // validate if the email matches our conditions
    if (validate_email) {
        sendAJAX("user_login", {
                "email": email,
                "password": password,
            },
            function (resp) {
                // set a cookie that you are logged in
                sessionStorage.setItem('status', 'loggedIn');

                //  check if you are trainer, then go to user verwaltung
                if(resp.is_trainer === true){
                    location.href="user_verwaltung"
                } else {
                    // ansonsten zeig nutzer ziele an
                    location.href="ziele/" + resp.user_id
                }
            }, function (status_code, message) {
                // show that your login was not successfully
                console.log(status_code);
                console.log(message);
                login_error.show()
            });
    }
}
