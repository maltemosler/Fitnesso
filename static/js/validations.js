function validateEmail(email, error_element) {
    const validate_email = /^([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x22([^\x0d\x22\x5c\x80-\xff]|\x5c[\x00-\x7f])*\x22)(\x2e([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x22([^\x0d\x22\x5c\x80-\xff]|\x5c[\x00-\x7f])*\x22))*\x40([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x5b([^\x0d\x5b-\x5d\x80-\xff]|\x5c[\x00-\x7f])*\x5d)(\x2e([^\x00-\x20\x22\x28\x29\x2c\x2e\x3a-\x3c\x3e\x40\x5b-\x5d\x7f-\xff]+|\x5b([^\x0d\x5b-\x5d\x80-\xff]|\x5c[\x00-\x7f])*\x5d))*$/.test(email);
    if (validate_email) {
        return true;
    } else {
        error_element.show();
        return false;
    }
}


function validatePassword(password, password_repeat, error_element, password_repeat_error) {
    var validate_pw = true;
    error_element.text("Your password must: \n");
    if (!/[A-Z]/.test(password)) {
        error_element.text(error_element.text() + "- Contain at least one uppercase letter (A-Z)\n");
        validate_pw = false;
    }
    if (!/[a-z]/.test(password)) {
        error_element.text(error_element.text() + "- Contain at least one lowercase letter (a-z)\n");
        validate_pw = false;
    }
    if (!/[0-9]/.test(password)) {
        error_element.text(error_element.text() + "- Contain at least one Digit (0-9)\n");
        validate_pw = false;
    }
    if (!/[^A-Za-z0-9]/.test(password)) {
        error_element.text(error_element.text() + "- Contain at least one Special character (~`!@#$%^&*()+=_-{}[]\\|:;”’?/<>,.)\n");
        validate_pw = false;
    }
    if (password.length < 8) {
        error_element.text(error_element.text() + "- Be a minimum of eight (8) characters in length \n");
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

function validateSettingsInviteCode(invite_code, error_element) {
    if (12 >= invite_code.length && invite_code.length >= 4) {
        error_element.hide();
        return true
    } else {
        error_element.show();
        return false
    }
}


function validateSettingsTradeUrl(trade_url, error_element) {
    if (80 >= trade_url.length && trade_url.length >= 70) {
        error_element.hide();
        return true
    } else {
        error_element.show();
        return false
    }
}

function validateSupportSubject(subject, error_element) {
    if (80 >= subject.length && subject.length >= 10) {
        error_element.hide();
        return true
    } else {
        error_element.text("Subject needs: " + (10 - subject.length).toString() + " more letters!");
        error_element.show();
        return false
    }
}

function validateSupportMessage(message, error_element) {
    if (5000 >= message.length && message.length >= 20) {
        error_element.hide();
        return true
    } else {
        error_element.text("Message needs: " + (20 - message.length).toString() + " more letters!");
        error_element.show();
        return false
    }
}

function validateVerificationCode(verification_code, error_element) {
    if (16 === verification_code.length) {
        error_element.hide();
        return true
    } else {
        error_element.show();
        return false
    }
}


function validateInviteCode(verification_code, error_element) {
    if (16 >= verification_code.length > 0) {
        error_element.hide();
        return true
    } else {
        error_element.show();
        return false
    }
}
