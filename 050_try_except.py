# -*- encoding=utf-8 -*-

while True:
    try:
        x=int(input('x = '))
    #except NameError:
        #print '输入内容必须为整数！'
    except ValueError:
        print '输入内容必须为整数！'
    else:
        break

while True:
    try:
        y=int(input('y = '))
    #except NameError:
        #print '输入内容必须为整数！'
    except ValueError:
        print '输入内容必须为整数！'
    else:
        break
        

print "x + y =", x+y
