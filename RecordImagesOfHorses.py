import keyboard
import time

def activate_scroll():
    keyboard.press_and_release('ctrl+alt+Q')
    time.sleep(1)  # Sleep for 1 second to simulate the scroll duratáion

#150px drop - on 1366x768
#Seperation = 2px
#Box = 75x75 px


# Example usage
activate_scroll()
