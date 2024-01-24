from PIL import Image


# Coordinates of the headshots
Personality = (430,345, 500,420)
# Directory Location
path = r"C:\Users\tcamp\Desktop\WildHorseIslands\Personalities\Sources"
# List of all current personalities
personalities = ["Clingy","Easy Going","Energetic","Grumpy","Independent","Lazy","Sassy","Spooky"]

# Iterate through all images
for personality in personalities:
    # File's location
    file = f"{path}\\{personality}Horse.png"
    # Open the image
    my_image = Image.open(file)
    # Crop the headshot
    cropped_image = my_image.crop(Personality)
    # File name
    filename = f"{path}\\{personality}.png"
    # Save the image
    cropped_image.save(filename)
