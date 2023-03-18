import nmapscan
import keylogger
import hashproducer
import passtester
import cesarcipher
from apptools import screen

def mainmenu():
    menu = """
    1- Nmap
    2- Keylogger
    3- Hash Encoder
    4- Password Tester
    5- Cesar Cipher
    6- Exit

    Note: This project is intended as educational material and should not be used for malicious purposes
    
    """
    key = 1 # Controler (if it is 0 exit)
    while key == 1:
        menu_input = int(input(menu))
        screen.clear()
        if menu_input == 1:
            if not nmapscan.nmap_menu():
                pass

        if menu_input == 2:
            if not keylogger.keylogger_menu():
                pass
            
        if menu_input == 3:
            if not hashproducer.hp_menu():
                pass

        if menu_input == 4:
            if not passtester.pt_menu():
                pass

        if menu_input == 5:
            if not cesarcipher.cesar_menu():
                pass

        if menu_input == 6:
            key = 0 # Exit from app
    else:
        print("Program shut down")


if __name__ == "__main__":
    mainmenu()