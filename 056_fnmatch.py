import fnmatch
import os
import re

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.txt'):
        print file

print '-----------------------------'
for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '*.Txt'):
        print file

print '-----------------------------'
for file in os.listdir('.'):
    if fnmatch.fnmatchcase(file, '*.txt'):
        print file       

print '-----------------------------'
for file in os.listdir('.'):
    if fnmatch.fnmatch(file, '[!a]*.txt'):
        print file

print '-----------------------------'
filename = "abc123.txt"
if fnmatch.fnmatch(filename, '[a-b]*.txt'):
    print filename, " match"

print '-----------------------------'
files = fnmatch.filter(os.listdir('.'), '*.txt')
print files


print '-----------------------------'
regex = fnmatch.translate('*.txt')
print regex
reobj = re.compile(regex)
reobj.match('abc123.txt')
print reobj
