import argparse

parser=argparse.ArgumentParser()
parser.add_argument('--output', type=argparse.FileType('wb',0))
print parser.parse_args(['--output', 'out'])
parser.add_argument('infile', type= argparse.FileType('r'))
print parser.parse_args(['-'])
