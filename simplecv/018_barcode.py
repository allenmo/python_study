'''
Install python-zbar, simplecv before run this program
'''

print __doc__

from SimpleCV import *
import time

cam = Camera()
#display = Display()

#while display.isNotDone():
while 1:
    img = cam.getImage()
    barcodes = img.findBarcode()
    #img.show()
    if type(barcodes) == FeatureSet and len(barcodes) >= 1:
        print "len:", time.time(), len(barcodes)
        for i in range(0,len(barcodes)):
            print barcodes[i].data
