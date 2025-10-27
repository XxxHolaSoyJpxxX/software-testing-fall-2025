import string

def pass_validator(password: str):
    error = ""
    special_chars = string.punctuation
    
    if len(password) < 8:
        error = "Password must be at least 8 characters"
    
    numbers = 0
    cap = 0
    spc = 0
    
    for val in password:
        if val.isdigit():
            numbers += 1
        if val.isupper():
            cap += 1
        if val in special_chars:
            spc += 1
    
    if numbers < 2:
        if error:
            error += "\n"
        error += "Password must contain at least 2 numbers"
    
    if cap == 0:
        if error:
            error += "\n"
        error += "Password must contain at least one capital letter"
    
    if spc == 0:
        if error:
            error += "\n"
        error += "Password must contain at least one special character"
    
    if error:
        return error
    return True
