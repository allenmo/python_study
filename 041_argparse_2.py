import argparse

parser = argparse.ArgumentParser(description="#####Learn from: http://python.usyiyi.cn/python_278/library/argparse.html#####")

parser.add_argument('integers', metavar='N', type=int, nargs='+', help= 'an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action= 'store_const', const=sum, default=max, help='sum the integers (default: find the max)')



parser.add_argument('--foo', help='foo of the %(prog)s program')
args = parser.parse_args()
print args
parser.print_help()
