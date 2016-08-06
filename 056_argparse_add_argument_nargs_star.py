import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--foo', nargs='*')
parser.add_argument('--bar', nargs='*')
parser.add_argument('baz', nargs='*')

print parser.parse_args('a b --foo x y --bar 1 2'.split())
