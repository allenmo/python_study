from SimpleCV import *

sleep_time = 2

print "Showing Greenscreen image"
greenscreen = Image("../static/images/green-screen-person.png")
greenscreen.show()
time.sleep(sleep_time)

print "Showing background image"
background = Image("../static/images/green-screen-wallst.png")
background.show()
time.sleep(sleep_time)

print "Showing Masked Image"
mask = greenscreen.hueDistance(color=Color.GREEN).binarize()
mask.show()
time.sleep(sleep_time)

print "Showing final image"
result = (greenscreen - mask) + (background - mask.invert())
result.show()
time.sleep(sleep_time)

