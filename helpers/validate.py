import re


def validate_email(email):
    regex = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
    return re.match(regex, email) is not None

def validate_cpf(cpf):
    valid_cpf = cpf.replace(".", "").replace("-", "")

    if len(valid_cpf) != 11 or not valid_cpf.isdigit():
        return False
    
    if len(set(valid_cpf)) == 1:
        return False

    total = 0
    for i in range(9):
        total += int(valid_cpf[i]) * (10 - i)
    

    first_digit = (total * 10) % 11
    if first_digit == 10 :
        first_digit = 0

    total = 0
    for i in range(10):
        total += int(valid_cpf[i]) * (11 - i)

    second_digit = (total * 10) % 11
    if second_digit == 10 :
        second_digit = 0

    validate = valid_cpf[-2:] == str(first_digit) + str(second_digit)

    if not validate :
        return False
    
    return valid_cpf

def validate_photo (filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

    print(filename)

    if filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS :
        return filename.rsplit('.', 1)[1]
    return False