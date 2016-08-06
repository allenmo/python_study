import argparse

parser=argparse.ArgumentParser()
parser.add_argument('--foo', default=42)
print parser.parse_args('--foo 2'.split())
print parser.parse_args(''.split())

parser.add_argument('--length', default='10', type=int)
parser.add_argument('--width', default=10.5, type=int)
print parser.parse_args()

parser.add_argument('koo', nargs='?', default=42)
print parser.parse_args('a'.split())
print parser.parse_args(''.split())

parser.add_argument('--yoo', default=argparse.SUPPRESS)
print parser.parse_args([])
print parser.parse_args(['--yoo','1'])
