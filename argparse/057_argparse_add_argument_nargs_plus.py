import argparse

parser = argparse.ArgumentParser()
parser.add_argument('foo', nargs='+')
print parser.parse_args('a b'.split())

print parser.parse_args(''.split())

