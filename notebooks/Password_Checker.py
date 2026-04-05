def is_strong_pwd(pwd):
    if len(pwd) < 8:
        return False
    if not any(i.isdigit() for i in pwd):
        return False
    if not any(i.isupper() for i in pwd):
        return False
    if not any(i.islower() for i in pwd):
        return False
    if not any(i in '!@#$%^&*?-' for i in pwd):
        return False
    return True

pwd = input("Enter a password: ")
if is_strong_pwd(pwd):
    print("Strong password")
else:
    print("Weak password")
