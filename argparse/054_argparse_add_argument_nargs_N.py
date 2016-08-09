import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--foo', nargs=2)
parser.add_argument('bar', nargs=1)
print parser.parse_args('c --foo a b'.split())

