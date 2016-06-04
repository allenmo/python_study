import sys
print("file name:", sys.argv[0])
for i in range(1, len(sys.argv)):
    print("parameter%d:%s" % (i, sys.argv[i]))
