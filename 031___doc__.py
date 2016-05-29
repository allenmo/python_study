#encoding=utf-8
import sys
type=sys.getfilesystemencoding()
def printMax(x, y):
    '''打印两个数中的最大值。
    两个值必须是整数。'''
    x = int(x)
    y = int(y)

    if x > y:
        print(x,unicode("最大"))
    else:
        print(y,unicode("最大"))

printMax(3, 5)
print(printMax.__doc__)

