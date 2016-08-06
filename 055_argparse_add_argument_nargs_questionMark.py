import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--foo', nargs='?', const='c', default='d')
parser.add_argument('bar', nargs='?', default='d')
print parser.parse_args('XX --foo YY'.split())

print parser.parse_args('XX --foo'.split())

print parser.parse_args(''.split())

