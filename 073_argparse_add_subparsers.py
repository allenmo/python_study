import argparse

parser=argparse.ArgumentParser(prog='PROG')
parser.add_argument('--foo', action='store_true', help='foo help')
subparsers=parser.add_subparsers(title='title of subcommands',
        description='descriiption of subcommands',
        help='sub-command help')

parser_a=subparsers.add_parser('a',help='a help')
parser_a.add_argument('bar', type=int, help='bar help')

parser_b=subparsers.add_parser('b', help='b help')
parser_b.add_argument('--baz', choices='XYZ', help='baz help')

print parser.parse_args(['a', '12'])
print parser.parse_args(['--foo', 'b', '--baz','Z'])

#print parser.parse_args(['--help'])
print parser.parse_args(['a', '--help'])
#print parser.parse_args(['b', '--help'])
