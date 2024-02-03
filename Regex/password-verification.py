def password_verification():
    password1 = input('Please enter a new password, between 8 to 15 characters: ')
    match = False
    while match is False:
        while len(password1) < 8 or len(password1) > 15:
            password1 = input('Password must be between 8 to 15 characters - please re-enter password: ')
        password2 = input('Please verify password: ')
        if password1 == password2:
            print('Password is valid')
            match = True

        else:
            print('Password is invalid')

    return match

password_verification()