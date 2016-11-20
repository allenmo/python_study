import sys
import time

for i in range(100):
    print 'Complete percent:' + str(i) + '%', 
    sys.stdout.write("\r")
    time.sleep(0.3)
