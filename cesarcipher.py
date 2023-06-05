from apptools import screen
def cesar_menu():
    menu = """
    1- Encrypting
    2- Decrypting
    3- Menu
    """
    key = 1
    upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_letters = "abcdefghijklmnopqrstuvwxyz"
    while key == 1:
        m_input = int(input(menu))
        screen.clear()
        
        if m_input == 1:
            message = input("Enter the message to encrypt: ") # Take message
            degree = int(input("Enter the shifting degree: ")) # Take shifting degree
            encrypted_message = ""

            for i in range(len(message)):
                character = message[i]

                if character.isupper():
                    indexn = upper_letters.index(character) # Check if the character is uppercase and control which letter then encrypt it
                    if (indexn + degree) > 25:
                        indexn = indexn - degree
                        encrypted_message += upper_letters[indexn]
                    else:
                        encrypted_message += upper_letters[indexn + degree]

                elif character.islower():
                    indexn = lower_letters.index(character) # Check if the character is lowercase and control which letter then encrypt it
                    if (indexn + degree) > 25:
                        indexn = indexn - degree
                        encrypted_message += lower_letters[indexn]
                    else:
                        encrypted_message += lower_letters[indexn + degree]

                else:
                    encrypted_message += character

            print("Encrypted text: " + encrypted_message )

        if m_input == 2:
            message = input("Enter the encrypted message: ")

            for degree in range(len(upper_letters)): # Shifting degree is unknown so that brute force used
                decrypted_message = ""
                for character in message:
                    if character in upper_letters: # Check if the character is uppercase and control which letter then decrypt it
                        indexn = upper_letters.index(character) - degree
                        decrypted_message += upper_letters[indexn]

                    elif character in lower_letters: # Check if the character is lowercase and control which letter then decrypt it
                        indexn = lower_letters.index(character) - degree
                        decrypted_message += lower_letters[indexn]

                    else:
                        decrypted_message += character

                print("Shifting degree %s," % (degree) + " Decrypted text: " + decrypted_message)

        if m_input == 3:
            key = 0
    else:
        screen.clear()
        return True