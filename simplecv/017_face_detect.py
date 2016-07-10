from SimpleCV import *

cam = Camera()
disp = Display()
size = cam.getImage().size()

segment = HaarCascade("face.xml")
while disp.isNotDone():
    img = cam.getImage()
    autoface = img.findHaarFeatures(segment)
    lenFace = len(autoface) 
    if ( lenFace > 0 ):
        for i in range(0,lenFace):
            face = autoface[i]
            x = face.x
            y = face.y
            width = face.width()
            height = face.height()
            img.dl().centeredRectangle((x,y),(width,height),Color.LIME)
        img.applyLayers()
    img.drawText("Num of Face: " + str(lenFace), x = size[0]-150, y = size[1]-30, color = Color.LIME, fontsize = 24)
    img.show()

