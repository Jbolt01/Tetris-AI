from PIL import Image, ImageGrab
from screen_select import find_BBox
import time

coords = find_BBox()
image = ImageGrab.grab()
image.show()