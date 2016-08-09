import argparse

parser=argparse.ArgumentParser(prog='PROG')
parser.add_argument('foo', type=int, choices=xrange(5,10))
print parser.parse_args('7'.split())
print parser.parse_args('11'.split())
