
def check_passwords_size(password):
    return len(str(password)) == 8


def check_passwords_isalnum(password):
    if str(password).isalpha()==False and str(password).isdigit()==False:
        return True
    else:
        return False
