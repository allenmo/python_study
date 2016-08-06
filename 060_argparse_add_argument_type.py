import argparse

parser=argparse.ArgumentParser()
parser.add_argument('--foo', type=int)
parser.add_argument('--bar', type=file)
print parser.parse_args('--foo 2 --bar temp.txt'.split())

parser.add_argument('--baz', type=argparse.FileType('w'))
print parser.parse_args('--baz temp.txt'.split())
