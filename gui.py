import sys
import os
from PIL import Image


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(
        os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


files = os.listdir("./Images/")

print(files)
for file in files:
    path = resource_path('./Images/'+file)
    logo = Image.open(path)
# When opening image
# logo = Image.open(path)
