import glob

print glob.glob(r"*.jpg")
#output something like: ['abc.jpg', 'aaa.jpg', 'bbb.jpg']

print glob.glob(r'../*.*')

print glob.glob(r'/*')

print glob.glob(r'/home/pi/*')

#---------------------------------
#iglob
#---------------------------------
fs = glob.iglob(r'*.jpg')

print fs

for f in fs:
    print f
