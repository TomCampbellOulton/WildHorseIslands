# Keyboard library to allow the program to activate the scrolling mechanic
import keyboard
# Mouse to simulate the button presses
import mouse
# Time to measure program efficiency and to slow the program
import time
# To take screenshots to check if all of the rows have been checked
from PIL import ImageGrab
# To read the screenshots to check if all of the rows have been checked
import pytesseract
# To get the current directory path
import os
# To get the current time for saving new files
from datetime import datetime

from pynput.mouse import Controller as MouseController
from pynput.mouse import Button
from pynput.keyboard import Controller as KeyboardController
from pynput.keyboard import Key

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
    time.sleep(0.3)
    mouse.release(Button.left)
# Initialise pytesseract by referring to it's exe file location
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\tcamp\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

time.sleep(2)
def activate_scroll():
    keyboard.press_and_release('ctrl+alt+Q')
    time.sleep(1)  # Sleep for 1 second to simulate the scroll duratáion

#150px drop - on 1366x768 and 1920x1080
#Seperation = 2px
#Box = 75x75 px

def take_screenshot(coords = (0,0, 1920,1080)):
    # Convert the coords to a list to manipulate
    coords = list(coords)
    # Trim the coords as they go 1 pixel over boundaries
    coords[2] -= 1
    coords[3] -= 1
    # Convert the coords back into a tuple
    coords = tuple(coords)

    # Grab the image of the specified size
    img = ImageGrab.grab(bbox=coords)
    # Return the image
    return img

    
def find_coords_boxes_in_given_row(number_of_horses_per_row = 10, size_of_boxes=(75,75), base_coordinates=(576,240), adjustment=(30,30), box_seperation=(2,2)):
    #576x240 = top left of first
    # Click 30 pixels in from each direction to ensure the correct horse is selected
    # X Coordinates:
    first_x_coord = base_coordinates[0] + adjustment[0]
    # Y Coordinates
    first_y_coord = base_coordinates[1] + adjustment[1]

    # Coordinates
    coords = []
    # Iterate through number of horses
    for i in range(number_of_horses_per_row):
        # Calculates the x and y coordinate as the coordinates of the first
        # plus the number of boxes over that needs to be looked at, starting from 0
        # Box seperation is the gap in between each box
        x = first_x_coord + (size_of_boxes[0] + box_seperation[0]) * i
        coordinates = (x,first_y_coord)
        # Appends the coordinates to the list
        coords.append(coordinates)

    return coords

def find_next_row(first_coord_prev_row=(576,240), base_coordinates=(576,240), size_of_boxes=(75,75), box_seperation=(2,2), scroll_size=150, adjustment=(30,30), number_of_horses_per_row=10):
    # Check if scrolling would work

    # Find top left of the previous row
    top_left_of_prev_row = (first_coord_prev_row[0] - adjustment[0], first_coord_prev_row[1] - adjustment[0])
    # Find the top left of this new row
    top_left_of_new_row = [top_left_of_prev_row[0], top_left_of_prev_row[1] + size_of_boxes[1] + box_seperation[1]]
    # Check y coordinate for scrolling down
    # If the y coord of the scroll would be above the base coordinates, don't scroll
    if (top_left_of_new_row[1] - scroll_size) < base_coordinates[1]:
        # Scroll
        activate_scroll()
        # Adjust the tuples to record this scroll
        top_left_of_new_row[1] = top_left_of_new_row[1] - scroll_size

    top_left_of_new_row = tuple(top_left_of_new_row)
    # New row is top_left_of_new_row
    # Find the coordinates
    coordinates_of_next_row = find_coords_boxes_in_given_row(base_coordinates = top_left_of_new_row, number_of_horses_per_row=number_of_horses_per_row,
                                                             size_of_boxes=size_of_boxes, adjustment=adjustment, box_seperation=box_seperation)
    print(coordinates_of_next_row)
    print(top_left_of_new_row)
    input()
    return coordinates_of_next_row

def check_if_remaining_rows(coords_for_equipment = (750,190, 1150,400)):
    # Takes a screenshot of the coords where equipment could be listed and checks to see if it's visible
    image = take_screenshot(coords_for_equipment)
    # Read the image
    text = pytesseract.pytesseract.image_to_string(image)
    # Check if "Equipment" is listed in the text
    print(text)
    if "Equipment" in text:
        return False
    else:
        return True

def close_horse_stats(coords=(750,240)):
    click(coords[0], coords[1])

def save_image(image, filename, filepath):
    name = f"{filepath}\\{filename}.png"
    image.save(name)

def check_each_horse_stats(coordinates=(606,270), screen_resolution=(1920, 1080)):
    # Click on the horse to open it's stats
    click(coordinates[0], coordinates[1])

    # Screenshot the stats page for that horse
    # If the screen resolution is 1920x1080
    if screen_resolution == (1920, 1080):
        screenshot = take_screenshot((219,250, 740,829))
        # Open the capture chance
        click(490,275)
        # Screenshot the findings
        screenshot2 = take_screenshot((617,360, 1302,709))
    elif screen_resolution == (1366,768):
        input("Wrong screen")
        screenshot = take_screenshot((155,177, 527,590))
        # Open the capture chance
        click(490,275)
        # Screenshot the findings
            #   !!!!!!!!!!!!!!!!!!!!! TO BE CORRECTED !!!!!!!!!!!!!!!!!!
        screenshot2 = take_screenshot((617,360, 1302,709))


    # Find the file path
    path = os.getcwd() + r"\UnprocessedHorses"
    # Find a new filename
    
    # Current time
    today = datetime.today()
    current_date = today.strftime('%Y_%m_%d_%H_%M_%S')
    filename = f"{current_date}_stats"
    filename2 = f"{current_date}_rarity"

    # Save the screenshots
    save_image(screenshot, filename, path)
    save_image(screenshot2, filename2, path)

    # Close the stats page on screen
    close_horse_stats()
    


def main(resolution = (1920,1080)):
    # Open the user's inventory
    #keyboard.press_and_release('tab')
    # 620x210 = open horses page
    # Open the horses menu
    #click(620,210)

    # If there are remaining rows
    #if check_if_remaining_rows():
    #    coordinates = find_next_row()
    #    # Iterate through each set of coordinates
    #    for coord in coordinates:
    #        check_each_horse_stats(coord, screen_resolution=resolution)
    if True:
        coordinates = find_next_row()
        # Iterate through each set of coordinates
        for coord in coordinates:
            check_each_horse_stats(coord, screen_resolution=resolution)

main()