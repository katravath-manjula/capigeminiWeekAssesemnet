def check_password(password):
    if len(password) < 8:
        return "Password must be at least 8 characters."

    k_upper =k_lower=kdigit =  k_special =False
    for char in password:
        if char.isupper():
            k_upper = True
        if char.islower():
            k_lower_lower = True
        if char.isdigit():
            k_digit = True
        if not char.isalnum():
            k_special = True

    if k_upper and k_lower and k_digit and k_special:
        return "Your password is strong"
    else:
        return "Password must include uppercase, lowercase, digits, and special characters."

password = input("Enter your password: ")
result = check_password(password)
print(result)