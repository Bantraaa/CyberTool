import hashlib
from apptools import screen

def hp_menu():
    menu = """
    Choose the hash type to convert
    1- MD5
    2- SHA-256
    3- SHA-512
    4- SHA-3-256
    5- SHA-3-512
    6- BLAKE2c
    7- BLAKE2b
    8- Menu
    """

    key = 1

    while key == 1:
        m_input = int(input(menu))
        screen.clear()
        if m_input == 8:
            key = 0
            
        text = input("Enter the text you want to encode: ")
        if m_input == 1:
            print("MD5:", hashlib.md5(text.encode()).hexdigest()) #Encoding text in MD5 hash type
        
        if m_input == 2:
            print("SHA-256:", hashlib.sha256(text.encode()).hexdigest())  #Encoding text in SHA-256 hash type

        if m_input == 3:
            print("SHA-512:", hashlib.sha512(text.encode()).hexdigest()) #Encoding text in SHA-512 hash type

        if m_input == 4:
            print("SHA-3-256:", hashlib.sha3_256(text.encode()).hexdigest()) #Encoding text in SHA-3-256 hash type

        if m_input == 5:
            print("SHA-3-512:", hashlib.sha3_512(text.encode()).hexdigest()) #Encoding text in SHA-3-512 hash type

        if m_input == 6:
            print("BLAKE2c:", hashlib.blake2s(text.encode()).hexdigest()) #Encoding text in BLAKE2c hash type

        if m_input == 7:
            print("BLAKE2b:", hashlib.blake2b(text.encode()).hexdigest()) #Encoding text in BLAKE2b hash type

    else:
        screen.clear()
        return True