password = input("Enter your password: ")

strength_score = 0

if password == "":
    print("Password cannot be empty.")

else:

    # Check password length
    if len(password) >= 8:
        strength_score += 1

    # Check for uppercase letter
    for current_character in password:

        if current_character.isupper():
            strength_score += 1
            break

    # Check for lowercase letter
    for current_character in password:

        if current_character.islower():
            strength_score += 1
            break

    # Check for number
    for current_character in password:

        if current_character.isdigit():
            strength_score += 1
            break

    # Check for special character
    special_characters = "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?"

    for current_character in password:

        if current_character in special_characters:
            strength_score += 1
            break

    # Determine password strength
    if strength_score <= 2:
        print("Your password is Weak.")

    elif strength_score <= 4:
        print("Your password is Medium.")

    else:
        print("Your password is Strong.")

    print("Password Strength Score:", strength_score, "/5")