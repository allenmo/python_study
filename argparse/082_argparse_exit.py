import argparse

parser=argparse.ArgumentParser()
parser.add_argument('--foo', default=42)
parser.add_argument('bar')
print parser.parse_args('kkk'.split())

print 'over'
parser.exit()

print 'over2'
