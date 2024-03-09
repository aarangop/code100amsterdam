import math
from functools import reduce
import requests

def calc_green_pixels(width, height):
    """
    Each image has an ellipse that is cut in 4. The ellipse's quarters are, however placed at the corners of the image. The green pixels are actually the corners of the image when the ellipse is in the middle.

    An ellipse can be parametrized with `a` and `b`, the major and minor half-axes, respectively, and it's area is given by pi * a * b. These correspond to half the width and height of the image.
    
    In order to calculate the green pixels we can calculate the area of the image and subtract the area of the ellipse that fits exactly into that image, with the width and the height as major/minor axes.
    """
    img_area = width * height
    ellipse_area = math.pi * width/2 * height/2

    return img_area - ellipse_area 

if __name__ == "__main__":

    images = requests.get("https://devrel.wearedevelopers.com/code100-puzzles/017-stars/stars.json").json()

    res = math.floor(reduce(lambda prev, img: prev + calc_green_pixels(img["width"], img["height"]), images, 0))

    print(f"There are {res} green pixels in the image.")