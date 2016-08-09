import argparse

parser=argparse.ArgumentParser(prog='PROG')
parser.add_argument('-x')
parser.add_argument('--foo')
print parser.parse_args('-x X'.split())
print parser.parse_args('--foo FOO'.split())

print parser.parse_args('--foo=fff'.split()) # option with more than 1 char, can use =

print parser.parse_args('-xX'.split()) # option with 1 char, option and value can concatenated

parser.add_argument('-a', action='store_true')
parser.add_argument('-b', action='store_true')
parser.add_argument('-c')
print parser.parse_args('-abcC'.split()) # only when the last option require a value, can concatenated and using one - prefix


