// all this functions are just validations
// first param is the user input and the second element is the error message element
// when validation is not successfully then the error element will show up
// this prevents unnecessary requests to our webserver

function validateEmail(email, error_element) {
    const validate_email = /^([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x22([^\x0d\x22\x5c\x80-\xff]|\x5c[\x00-\x7f])*\x22)(\x2e([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x22([^\x0d\x22\x5c\x80-\xff]|\x5c[\x00-\x7f])*\x22))*\x40([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x5b([^\x0d\x5b-\x5d\x80-\xff]|\x5c[\x00-\x7f])*\x5d)(\x2e([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x5b([^\x0d\x5b-\x5d\x80-\xff]|\x5c[\x00-\x7f])*\x5d))*$/.test(email);
    if (validate_email) {
        error_element.hide();
        return true;
    } else {
        error_element.show();
        return false;
    }
}


function validatePassword(password, password_repeat, error_element, password_repeat_error) {
    var validate_pw = true;
    error_element.text("Dein Passwort muss: \n");
    if (!/[A-Z]/.test(password)) {
        error_element.text(error_element.text() + "- Mindestens ein Großbuchstaben enthalten (A-Z)\n");
        validate_pw = false;
    }
    if (!/[a-z]/.test(password)) {
        error_element.text(error_element.text() + "- Mindestens ein Kleinbuchstaben enthalten (a-z)\n");
        validate_pw = false;
    }
    if (!/[0-9]/.test(password)) {
        error_element.text(error_element.text() + "- Mindestens eine Zahl enthalten (0-9)\n");
        validate_pw = false;
    }
    if (!/[^A-Za-z0-9]/.test(password)) {
        error_element.text(error_element.text() + "- Mindestens ein Sonderzeichen enthalten (~`!@#$%^&*()+=_-{}[]\\|:;”’?/<>,.)\n");
        validate_pw = false;
    }
    if (password.length < 8) {
        error_element.text(error_element.text() + "- Eine Länge von mehr als 8 haben \n");
        validate_pw = false;
    }
    if (validate_pw) {
        error_element.hide();
    } else {
        error_element.show();
    }

    if (password === password_repeat) {
        password_repeat_error.hide();
    } else {
        password_repeat_error.show();
        validate_pw = false
    }
    return validate_pw
}


function validateFirstName(name, error_element) {
    if (30 > name.length && name.length > 1) {
        error_element.hide();
        return true
    } else {
        error_element.show();
        return false
    }
}

function validateSecondName(name, error_element) {
    if (30 > name.length && name.length > 1) {
        error_element.hide();
        return true
    } else {
        error_element.show();
        return false
    }
}

function validateZiel(ziel, error_element) {
    if (128 >= ziel.length && ziel.length >= 2) {
        error_element.hide();
        return true
    } else {
        error_element.show();
        return false
    }
}
