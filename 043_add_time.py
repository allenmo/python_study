import time

while True:
    inputStr=raw_input("Input time(e.g.2016-08-09 12:30:59):")
    print "You input    :", inputStr
    t1=time.mktime(time.strptime(inputStr, "%Y-%m-%d %H:%M:%S"))
    t2=t1+5*60+30
    output=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t2))
    print "After 5min30s:", output
