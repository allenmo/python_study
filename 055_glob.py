import glob

print  r'glob.glob(r"*.jpg")', "\n", glob.glob(r"*.jpg"), "\n"
#output something like: ['abc.jpg', 'aaa.jpg', 'bbb.jpg']

print r"glob.glob(r'../*.*')", "\n", glob.glob(r'../*.*'), "\n"

print r"glob.glob(r'/*')", "\n", glob.glob(r'/*'), "\n"

print r"glob.glob(r'/home/pi/*')", "\n", glob.glob(r'/home/pi/*'), "\n"

print r"glob.glob(r'mv.jpg*')", "\n", glob.glob(r'mv.jpg*'), '\n'

print r"glob.glob(r'[m-r]*')", "\n", glob.glob(r'[m-r]*'), "\n"

print r"glob.glob(r'[!m-r]*')", "\n", glob.glob(r'[!m-r]*'), "\n"

#---------------------------------
#iglob
#---------------------------------
fs = glob.iglob(r'*.jpg')

print fs

for f in fs:
    print f
