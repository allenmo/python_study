from sys import *
from SimpleCV import *
cam = Camera()
disp = Display()

while disp.isNotDone():
    prev = cam.getImage()
    time.sleep(0.05)
    current = cam.getImage()
    diff = (current - prev) * 10
    #if disp.mouseLeft:
    #    break
    diff.save(disp)
sys.exit()
