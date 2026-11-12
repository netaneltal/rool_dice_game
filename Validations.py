def check_name(name):
    if name == "":
        return False
    elif type(name) == int:
        return False
    else:
        return True

def check_number(number):
    num = number.isdigit()
    if num > 0 or num <11:
           return num
    return False