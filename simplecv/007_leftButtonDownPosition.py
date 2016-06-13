from SimpleCV import *
import time

disp = Display((640, 480))
cam = Camera()
while(disp.isNotDone()):
    img = cam.getImage()
    dwn = disp.leftButtonDownPosition()
    up = disp.leftButtonUpPosition()
    n = 0 
    if( dwn is not None):
        print("in if")
        pt2 = (dwn[0]+100, dwn[1]+100)
        bb = disp.pointsToBoundingBox(dwn, pt2)
        img.drawRectangle(bb[0], bb[1], bb[2], bb[3] )
        img.drawText("kkk") 
        n = 0.2 
    #img.drawText("he123")
    print(dwn, up)
    img.save(disp)
    time.sleep(n)

