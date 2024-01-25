from pynput.mouse import Controller as MouseController
from pynput.mouse import Button
from pynput.keyboard import Controller as KeyboardController
from pynput.keyboard import Key
import time

mouse = MouseController()
keyboard = KeyboardController()
def focus_window():
    with keyboard.pressed(Key.alt):
        keyboard.press(Key.tab)
        time.sleep(0.1)
        keyboard.release(Key.tab)
        time.sleep(0.1)
def click(x, y, duration_of_click=0.2, left_or_right="left"):
    mouse.position = (x, y)
    time.sleep(duration_of_click)
    mouse.press(Button.left)
    time.sleep(0.1)
    mouse.release(Button.left)

# Open the horses menu
time.sleep(1)


# Click at the specified coordinates
mouse.position = (750,240)
mouse.press(Button.left)
mouse.release(Button.left)
focus_window()

click(750, 240)
click(750, 240)
