'''
Install python-zbar, simplecv before run this program
'''

print __doc__

from SimpleCV import *

cam = Camera()
display = Display()

while display.isNotDone():
    img = cam.getImage()
    barcodes = img.findBarcode()
    img.show()
    if barcodes and len(barcodes)==1:
        data = barcodes[0].data
        print data
