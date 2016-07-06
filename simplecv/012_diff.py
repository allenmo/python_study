from sys import *
from SimpleCV import *
cam = Camera()
disp = Display()

threshold = 1.3 
sumMean = 0
noPic = 100
for i in range(0,noPic):
    one = cam.getImage()
    time.sleep(0.05)
    two = cam.getImage()
    diff = two - one
    matrix = diff.getNumpy()
    mean = matrix.mean()
    sumMean = sumMean + mean
mean = sumMean / noPic
threshold = sumMean / noPic + 0.5
print mean, "mean value-----------------------"
print threshold, "threshold value------------------------------"

while disp.isNotDone():
    prev = cam.getImage()
    time.sleep(0.05)
    current = cam.getImage()
    diff = (current - prev) * 10
    matrix = diff.getNumpy()
    mean = matrix.mean()/10
    #if disp.mouseLeft:
    #    break
    diff.save(disp)

    if mean >= threshold:
        print mean,"Motion Detected"
        ti = time.time()
        theTime = time.localtime(ti)
        mti = ti - int(ti)
        theTimeStr = str(theTime[0]) + "-" + str(theTime[1]) + "-" + str(theTime[2]) + "-" + str(theTime[3]) + "_" + str(theTime[4]) + "_" + str(theTime[5] + mti) + ".png"
        current.save(theTimeStr)
    else:
        print mean
sys.exit()
