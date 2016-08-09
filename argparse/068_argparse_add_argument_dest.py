import argparse

parser=argparse.ArgumentParser()
parser.add_argument('bar')
print parser.parse_args('XXX'.split())

parser.add_argument('-f', '--foo-bar', '--foo')
parser.add_argument('-x', '-y')
print parser.parse_args('XXX -f 1 -x 2'.split())
print parser.parse_args('XXX --foo 1 -y 2'.split())

parser.add_argument('--koo', dest='kkk')
print parser.parse_args('XXX --foo 1 -y 2 --koo ppp'.split())
