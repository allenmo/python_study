import os
import glob
import time
from SimpleCV import *

print __doc__

#Settings
v = sys.argv
n = len(v)
if n == 3:
    my_images_path = sys.argv[1]
    extension = "*." + sys.argv[2]
elif n == 2:
    my_images_path = sys.argv[1]
    extension = "*.jpg"
else:
    my_images_path = "/home/allen/Pictures"
    extension = "*.png"

#Program
if not my_images_path:
    path = os.getcwd()
else:
    path = my_images_path

imgs = list()
directory = os.path.join(path, extension)
files = glob.glob(directory)

for file in files:
    new_img = Image(file)
    new_img.show()
    time.sleep(2)
