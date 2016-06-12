from SimpleCV import *

display = Display(resolution = (800, 600))
cam = Camera()
done = False
flip = False
while not display.isDone():
    if flip:
        cam.getImage().flipHorizontal().save(display)
    else:
        cam.getImage().save(display)
    if display.mouseLeft:
        flip = not flip
    if display.mouseRight:
        display.done = True

