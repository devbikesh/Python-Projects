def encrypt_message(message, shift):

    encrypted_message = ""

    for character in message:

        if character.islower():

            alphabet_position = ord(character) - ord("a")

            new_position = (alphabet_position + shift) % 26

            shifted_character = chr(new_position + ord("a"))

            encrypted_message += shifted_character

        elif character.isupper():

            alphabet_position = ord(character) - ord("A")

            new_position = (alphabet_position + shift) % 26

            shifted_character = chr(new_position + ord("A"))

            encrypted_message += shifted_character

        else:

            encrypted_message += character

    return encrypted_message


def decrypt_message(message, shift):

    decrypted_message = ""

    for character in message:

        if character.islower():

            alphabet_position = ord(character) - ord("a")

            new_position = (alphabet_position - shift) % 26

            shifted_character = chr(new_position + ord("a"))

            decrypted_message += shifted_character

        elif character.isupper():

            alphabet_position = ord(character) - ord("A")

            new_position = (alphabet_position - shift) % 26

            shifted_character = chr(new_position + ord("A"))

            decrypted_message += shifted_character

        else:

            decrypted_message += character

    return decrypted_message


while True:

    print("\n1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")

    user_choice = int(input("Enter your choice: "))

    if user_choice == 1:

        message = input("Enter the message to encrypt: ")

        shift = int(input("Enter the shift value: "))

        encrypted_message = encrypt_message(message, shift)

        print("Encrypted message:", encrypted_message)

    elif user_choice == 2:

        message = input("Enter the message to decrypt: ")

        shift = int(input("Enter the shift value: "))

        decrypted_message = decrypt_message(message, shift)

        print("Decrypted message:", decrypted_message)

    elif user_choice == 3:

        print("Goodbye!")

        break

    else:

        print("Invalid choice. Please try again.")