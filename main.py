import math
from functools import reduce
import requests

def ellipse_area(major_axis, minor_axis):
    return math.pi * major_axis * minor_axis

def image_area(width, height):
    return width * height

def number_of_green_pixels(width, height):
    return image_area(width, height) - ellipse_area(width/2, height/2)

if __name__ == "__main__":

    """
    Each image has an ellipse that is cut in 4. The ellipse's quarters are, however placed at the corners of the image. The green pixels are actually the corners of the image when the ellipse is in the middle.

    An ellipse can be parametrized with `a` and `b`, the major and minor half-axes, respectively, and it's area is give by pi * a * b. These correspond to half the width and height of the image.

    In order to calculate the green pixels we can calculate the area of the image and subtract the area of the ellipse that fits exactly into that image, with the width and the height as major/minor axes.
    """

    images = requests.get("https://devrel.wearedevelopers.com/code100-puzzles/017-stars/stars.json").json()

    result = sum([number_of_green_pixels(image['width'], image['height']) for image in images])

    result_rounded = math.floor(result)

    print(f"There are {result_rounded} green pixels in the image.")