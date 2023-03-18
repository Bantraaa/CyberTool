import re
from apptools import screen

def pt_menu():
    menu = """
    1- Start password testing
    2- Menu
    """

    key = 1

    while key == 1:
        m_input = int(input(menu))
        screen.clear()
        if m_input == 1:

            def passtest(password):
                uppercase_check = 0
                number_check = 0
                punctuation_check = 0
                length = len(password)

                if length >= 8:
                    length_check = 1
                for i in range(length):
                    if re.search(r"[A-Z]", password):
                        uppercase_check = 1

                    if re.search(r"\d", password):
                        number_check = 1

                    if re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', password):
                        punctuation_check = 1

                scale = uppercase_check + number_check + punctuation_check + length_check

                if scale <= 1:
                    print("Your password is too weak")
                
                elif scale == 2:
                    print("Your password is weak")

                elif scale == 3:
                    print("Your password has medium strength")

                elif scale == 4:
                    print("Your password is strong")

            passtest(password = input("Enter your password: "))

        if m_input == 2:
            key = 0

    else:
        screen.clear()
        return True