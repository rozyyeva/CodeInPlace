"""
File: forestfire.py
----------------
This program highlights fires in an image by identifying
pixels who red intensity is more than INTENSITY_THRESHOLD times
the average of the red, green, and blue values at a pixel.
Those "sufficiently red" pixels are then highlighted in the
image and the rest of the image is turned grey, by setting the
pixels red, green, and blue values all to be the same average
value.
"""


# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage

DEFAULT_FILE = 'images/greenland-fire.png'

def find_flames(filename):
    """
    This function should highlight the "sufficiently red" pixels
    in the image and grayscale all other pixels in the image
    in order to highlight areas of wildfires.
    """
    image = SimpleImage(filename)

    # For each pixel in the image, calculate the average of three RGB values
    for px in image:
        avg = (px.red + px.green + px.blue) / 3
        # If the red value is less than the calculated average,
        # assign the average to all of three RGB values.
        # Else, set the red value to 255 and other two values to 0.
        if px.red < avg:
            px.red = avg
            px.green = avg
            px.blue = avg
        else:
            px.red = 255
            px.green = 0
            px.blue = 0

    # Return recolored image
    return image


def main():
    # Get file and load image
    filename = get_file()

    # Show the original fire
    original_fire = SimpleImage(filename)
    original_fire.show()

    # Show the highlighted fire
    highlighted_fire = find_flames(filename)
    highlighted_fire.show()

    
def get_file():
    # Read image file path from user, or use the default file
    filename = input('Enter image file (or press enter): ')
    if filename == '':
        filename = DEFAULT_FILE
    return filename


if __name__ == '__main__':
    main()
