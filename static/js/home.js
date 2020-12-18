function login() {
    const login_error = $("#login-error-text");

    const email = $("#login-email").val();
    const password = $("#login-password").val();

    const validate_email = validateEmail(email, login_error);

    if (validate_email) {
        sendAJAX("user_login", {
                "email": email,
                "password": password,
            },
            function (resp) {
                console.log("logged in");
                sessionStorage.setItem('status', 'loggedIn');

                //  check if trainer - go to user verwaltung
                if(resp.is_trainer === true){
                    location.href="user_verwaltung"
                } else {
                    location.href="ziele/" + resp.user_id
                }
            }, function (status_code, message) {
                console.log("tjgwerz");
                console.log(status_code);
                console.log(message);
                login_error.show()
            });
    }
}
