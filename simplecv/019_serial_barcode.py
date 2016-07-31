'''
Make sure installed:[ python-zbar, simplecv ] before run this program
'''

print __doc__

from SimpleCV import *
import serial
import time

cam = Camera()
#display = Display()
ser = serial.Serial("/dev/ttyUSB0",9600)

def serialRxLoop():
    while True:
        count = ser.inWaiting()
        if count != 0:
            print "count:", count
            recv = ser.read(count)
            sn = readSN()
            ser.write(sn + "\r\n")
            print "!!!!", sn, "####"

        print "Waiting ......[", time.time(), "]"
        ser.flushInput()
        time.sleep(0.1)

def readSN():
    ok = False
    n = 0

    while(ok == False and n < 50):
        img = cam.getImage()
        barcodes = img.findBarcode()
        if type(barcodes) == FeatureSet and len(barcodes) >=1:
            ok = True
            return barcodes[0].data
        else:
            ok = False
            #return ""
        n = n + 1
    return ""

serialRxLoop()
