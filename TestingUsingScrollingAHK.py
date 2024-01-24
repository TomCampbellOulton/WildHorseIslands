import keyboard
import time

def press_ctrl_alt_s():
    keyboard.press_and_release('ctrl+alt+s')
    time.sleep(1)  # Sleep for 1 second to simulate the scroll duratáion

# Example usage
press_ctrl_alt_s()
