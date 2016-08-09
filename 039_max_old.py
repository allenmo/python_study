import sys

'''
Input 2 int/float in the command line,
and program will out put the max one
'''
print __doc__

count = len(sys.argv)
if count == 3:
    x = sys.argv[1]
    y = sys.argv[2]
    print "x, y:", x, y
    if isinstance(x, (int, float)) and isinstance(y, (int, float)):
        if x > y:
            z = x
        else:
            z = y
        print z
    else:
        raise TypeError('bad operand type of in put value')
else:
    raise ValueError('need 2 parameter to compare!')

