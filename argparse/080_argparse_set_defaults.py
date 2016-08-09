import argparse

parser=argparse.ArgumentParser()
parser.add_argument('--foo', type=int)
parser.set_defaults(bar=42, baz='badger')
print parser.parse_args(['--foo','789'])

parser.add_argument('--koo', default='kkk')
parser.set_defaults(koo='ppp')
print parser.parse_args(['--foo', '789'])
