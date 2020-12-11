import re


def validate_first_name(name):
    if 30 > len(name) > 1:
        return True
    else:
        return False


def validate_last_name(name):
    if 30 > len(name) > 1:
        return True
    else:
        return False


def validate_email(email):
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email)
    if match:
        return True
    else:
        return False


def validate_password(password):
    if re.search('[0-9]', password) is None:
        return False
    if re.search('[A-Z]', password) is None:
        return False
    if re.search('[a-z]', password) is None:
        return False
    if len(password) < 8:
        return False
    return True


def validate_trade_url(trade_url):
    if 80 >= len(trade_url) >= 70:
        return True
    return False


def validate_invite_code(invite_code):
    if 16 >= len(invite_code) >= 0:
        return True
    return False
