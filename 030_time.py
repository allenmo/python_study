import time

ISOTIMEFORMAT='%Y-%m-%d %X'
print('time.time():%s'% time.time())
print('time.localtime():', time.localtime())
print('time.strftime(..localtime..):%s'% time.strftime(ISOTIMEFORMAT, time.localtime()))
print('time.strftime(..gmtime..):%s'% time.strftime(ISOTIMEFORMAT, time.gmtime(time.time())))
print('time.timezone:%s'% time.timezone)
zone = time.timezone/3600
print('time.timezone/3600:%s'%zone)
