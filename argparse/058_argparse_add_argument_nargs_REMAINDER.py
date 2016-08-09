import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--foo')
parser.add_argument('command')
parser.add_argument('args', nargs=argparse.REMAINDER)
print parser.parse_args('--foo B cmd --arg1 XX ZZ'.split())

