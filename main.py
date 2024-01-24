import os
import imagehash
from PIL import Image
import pytesseract
# Setup tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\tcamp\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
folder_path_for_personalities = r"C:\Users\tcamp\Desktop\WildHorseIslands\Personalities\Headshots"


def dhash(image, hash_size=4):
    # Calculate the difference hash (dhash) for an image
    return imagehash.dhash(image, hash_size=hash_size)

def compare_images(new_image, folder_path):
    try:
        # Calculate the hash for the new image
        new_hash = dhash(new_image)
        # Iterate through images in the folder
        best_match = None
        best_similarity = float('inf')
        for filename in os.listdir(folder_path):
            if filename.endswith(".png"):
                # Calculate the hash for the saved image
                saved_image_path = os.path.join(folder_path, filename)
                saved_image = Image.open(saved_image_path)
                saved_hash = dhash(saved_image)

                # Calculate the Hamming distance between the hashes
                hamming_distance = new_hash - saved_hash

                # Update best match if the current image is more similar
                if hamming_distance < best_similarity:
                    best_similarity = hamming_distance
                    best_match = saved_image_path

        return best_match, best_similarity
    except:
        print( "Error D:")
        return None, None

# Define the parameters
def get_stats_coords(image):
    # Size of image
    image_size = image.size
    # If the resolution is 1366x768
    if image_size == (1366, 768):

        Coat = (200,320, 300, 350)
        Mane = (200,350, 300,380)
        Tail = (200,380, 300,410)

        Personality = (306,247, 360,300)
        Sex = (360,280, 410,300)
        Height = (410,280, 460,300)

        Speed = (305,340, 370,360)
        Stamina = (370,340, 436,360)
        Strength = (438,340, 502,360)

        Jump = (305,395, 370,415)
        Agility = (370,395, 436,415)
        Happiness = (436,395, 502,415)

        Purity = (180,480, 260,500)
        Bond = (260,480, 340, 500)

    # If the resolution is 1920x1080
    elif image_size == (1920,1080):
        Coat = (280,450, 410, 490)
        Mane = (280,490, 410,530)
        Tail = (280,530, 410,574)

        Personality = (430,345, 500,420)
        Sex = (500,390, 580,420)
        Height = (580,390, 650,420)

        Speed = (425,485, 520,510)
        Stamina = (520,485, 615,510)
        Strength = (615,485, 710,510)

        Jump = (425,550, 520,580)
        Agility = (520,550, 615,580)
        Happiness = (615,550, 710,580)

        Purity = (250,640, 360,660)
        Bond = (365,640, 480, 660)

    # Unsupported size
    else:
        print("This size is not supported :c")
    
    # Store all the areas in a list
    key_areas = (Coat, Mane, Tail, Personality, Sex, Height, Speed, Stamina, Strength, Jump, Agility, Happiness, Purity, Bond)

    # Return the coords
    return key_areas

class Horse:
    def __init__(self):
        self._coat = 0
        self._mane_colour = ""
        self._mane_length = ""
        self._tail_colour = ""
        self._tail_length = ""
        self._personality = 0
        self._sex = 0
        self._height = 0
        self._speed = 0
        self._stamina = 0
        self._strength = 0
        self._jump = 0
        self._agility = 0
        self._happiness = 0
        self._purity = 0
        self._bond = 0
        self._chance_of_capture = 0
    
    def get_coat(self):
        return self._coat
    
    def set_coat(self, coat):
        self._coat = coat

    def get_mane(self):
        return (self._mane_colour, self._mane_length)

    def set_mane(self, mane):
        self._mane_colour = mane[0]
        self._mane_length = mane[1]

    def get_tail(self):
        return (self._tail_colour, self._tail_length)

    def set_tail(self, tail):
        self.tail_colour = tail[0]
        self.tail_length = tail[1]

    # Getters
    def get_personality(self):
        return self._personality

    def get_sex(self):
        return self._sex

    def get_height(self):
        return self._height

    def get_speed(self):
        return self._speed

    def get_stamina(self):
        return self._stamina

    def get_strength(self):
        return self._strength

    def get_jump(self):
        return self._jump

    def get_agility(self):
        return self._agility

    def get_happiness(self):
        return self._happiness

    def get_purity(self):
        return self._purity

    def get_bond(self):
        return self._bond
    
    def get_capture_chance(self):
        return self._chance_of_capture

    # Setters
    def set_personality(self, value):
        self._personality = value

    def set_sex(self, value):
        self._sex = value

    def set_height(self, value):
        self._height = value

    def set_speed(self, value):
        self._speed = value

    def set_stamina(self, value):
        self._stamina = value

    def set_strength(self, value):
        self._strength = value

    def set_jump(self, value):
        self._jump = value

    def set_agility(self, value):
        self._agility = value

    def set_happiness(self, value):
        self._happiness = value

    def set_purity(self, value):
        self._purity = value

    def set_bond(self, value):
        self._bond = value

    def set_capture_chance(self, value):
        self._chance_of_capture = value

def convert_to_binary_black_and_white_in_memory(original_image, threshold=128):
    try:
        # Convert the image to grayscale
        grayscale_image = original_image.convert('L')

        # Create a new blank image with the same size
        binary_image = Image.new("RGB", grayscale_image.size)

        # Iterate through each pixel and set the color based on the threshold
        for x in range(grayscale_image.width):
            for y in range(grayscale_image.height):
                # Get the grayscale value of the pixel
                pixel_value = grayscale_image.getpixel((x, y))

                # Determine the color based on the threshold
                color = (255, 255, 255) if pixel_value >= threshold else (0, 0, 0)

                # Set the color in the new image
                binary_image.putpixel((x, y), color)

        return binary_image

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def read_data(image, key_areas, folder_path_for_personalities):
    data_read = []

    # Counter for completed iterations
    counter = 0
    # Get the text for each stat
    for area in key_areas:
        cropped_image = image.crop(area)
        # If the stat is personality, use image recognition instead
        if counter == 3:
            # Find the personality
            best_match, similarity_score = compare_images(cropped_image, folder_path_for_personalities)
            # Convert the best_match from path to personality name
            file_name = best_match.split("\\")[-1]
            # Remove the .png
            personality_type = file_name.split(".png")[0]
            data_read.append(personality_type)
        else:
            # Image size
            width, height = cropped_image.size
            # Enlarge image by 25 times
            new_image = cropped_image.resize((10*width, 10*height))
            text = pytesseract.pytesseract.image_to_string(new_image)
            data_read.append(text)
        counter += 1
    # Record this data
            
    #Return the data
    return data_read

# Process my image
def process_image(image):
    # Identify the areas for each component of the horses stats
    key_areas = get_stats_coords(image)
    # Read the stats
    horse_data = read_data(image, key_areas, folder_path_for_personalities)
    # Create the horse
    horse = Horse()
    # Set the horses stats
    set_horse_stats(horse, horse_data)
    return horse

def set_horse_stats(horse, stats):
    # Set the coat
    horse.set_coat = stats[0]

    # Seperate the mane length and colour
    mane_colour, mane_length = check_hair_colour(stats[1])
    mane = (mane_colour, mane_length)
    horse.set_mane(mane)

    # Seperate the tail length and colour
    tail = check_hair_colour(stats[2])
    horse.set_tail(tail)

    # Set the horses stats
    horse.set_personality(stats[3])
    horse.set_sex(stats[4])
    horse.set_height(stats[5])
    horse.set_speed(stats[6])
    horse.set_stamina(stats[7])
    horse.set_strength(stats[8])
    horse.set_jump(stats[9])
    horse.set_agility(stats[10])
    horse.set_happiness(stats[11])
    horse.set_purity(stats[12])
    horse.set_bond(stats[13])


def check_hair_colour(value):
    file = open("Hair Colours.txt", "r")
    legal_colours = file.readlines()
    file.close()
    # Default for style and colour to be null
    style = colour = None

    #Check each hair colour
    for hair_colour in legal_colours:
        # Remove the special character \n
        hair_colour = hair_colour.replace("\n","")

        # Check the colour is not a comment
        # If the hair colour is in the input
        if (("#" in hair_colour) == False) and (hair_colour in value):
            # Seperate the colour and style
            colour = hair_colour
            style = value.replace(colour, "").replace(" \n","")
    
    return (colour, style)

# List of hair colours
hair_colours = []
# List of hair lengths
hair_lengths = []

# List of all horses recorded 
horses = []

my_image = Image.open('image_2.png')
horses.append(process_image(my_image))
print(horses[0].get_height())