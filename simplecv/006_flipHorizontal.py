from SimpleCV import *
import time

display = Display(resolution = (800, 600), title="haha", displaytype='tandard')
cam = Camera()
done = False
flip = False
while not display.isDone():
    if flip:
        cam.getImage().flipHorizontal().save(display)
    else:
        cam.getImage().save(display)
    time.sleep(0.02)
    if display.mouseLeft:
        flip = not flip
    if display.mouseRight:
        display.done = True

