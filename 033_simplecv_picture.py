import time
from SimpleCV import Camera

cam = Camera()
time.sleep(0.2)
img = cam.getImage()
img.save("simplecv_picture.png")
#cam.close()

