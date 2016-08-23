import linecache

print linecache.getline('052_linecache.py',2)

lines = linecache.getlines('052_linecache.py')
print lines
print len(lines)
