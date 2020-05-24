"""
This program generates the Warhol effect based on the original image.
"""

import random
from simpleimage import SimpleImage


N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'


def main():
    # Create a blank Image with a given width and height
    final_image = SimpleImage.blank(WIDTH, HEIGHT)
    for y in range(N_COLS):
        for x in range(N_ROWS):
            # Generate the random numbers to scale RGB values
            red_scale = random.randint(0, 5) / 3
            green_scale = random.randint(0, 5) / 3
            blue_scale = random.randint(0, 5) / 3
            # Create a patch with those random scale values
            patch = make_recolored_patch(red_scale, green_scale, blue_scale)
            # Apply the patch to the final image
            apply_colored_patch(
                final_image,
                PATCH_SIZE * x,
                PATCH_SIZE * y,
                patch
            )
    # Show the final image
    final_image.show()


def apply_colored_patch(image, row, col, patch):
    """
    This function applies the patch on the given image starting at the given row
    and column of the image.
    :param image: Image that will be patched
    :param row: Row of the image at which the patch will be applied
    :param col: Column of the image at which the patch will be applied
    :param patch: Patch that will be applied to the image
    """
    for y in range(PATCH_SIZE):
        for x in range(PATCH_SIZE):
            pixel = patch.get_pixel(x, y)
            image.set_pixel(x + col, y + row, pixel)


def make_recolored_patch(red_scale, green_scale, blue_scale):
    """
    Implement this function to make a patch for the Warhol Filter. It
    loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixels' red component by
    :param green_scale: A number to multiply each pixels' green component by
    :param blue_scale: A number to multiply each pixels' blue component by
    :return: the newly generated patch
    """
    patch = SimpleImage(PATCH_NAME)
    for px in patch:
        px.red = px.red * red_scale
        px.green = px.green * green_scale
        px.blue = px.blue * blue_scale
    return patch


if __name__ == '__main__':
    main()
