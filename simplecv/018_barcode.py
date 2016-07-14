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
    if type(barcodes) == FeatureSet and len(barcodes) == 1:
        print barcodes[0].data
