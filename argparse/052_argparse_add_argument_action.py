import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-b','--bar', action='store')

parser.add_argument('--kkk','-k', action='store_const', const=42)

parser.add_argument('--ttt','-t', action='store_true')
parser.add_argument('--fff','-f', action='store_false')

parser.add_argument('--appe', '-a', action='append')
parser.add_argument('--appec', '-c', dest='app', action='append_const', const='abc')
parser.add_argument('--appec2', '-C', dest='app', action='append_const', const='123')
parser.add_argument('--appec3', '-s', dest='app', action='append_const', const=str)
parser.add_argument('--appec4', '-i', dest='app', action='append_const', const=int)

parser.add_argument('--number', '-n', dest='the_num', action='count')

parser.add_argument('--version', '-v', action='version', version='%(prog)s 2.0')

args = parser.parse_args()
print args
