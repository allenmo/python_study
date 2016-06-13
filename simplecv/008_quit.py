from SimpleCV import *
import time

img = Image("simplecv")
d = img.show()
print(d)
print(d.resolution)
time.sleep(5)
d.quit()
