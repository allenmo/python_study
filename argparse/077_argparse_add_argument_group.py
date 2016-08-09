import argparse

parser=argparse.ArgumentParser(prog='PROG', add_help=False)
group1=parser.add_argument_group('group1')
group1.add_argument('--foo', help='foo help')
group1.add_argument('bar', help='bar help')

group2=parser.add_argument_group('group2', 'group2 description')
group2.add_argument('bar', help='bar help')

parser.add_argument('--kkk', help='kkk help for default optional argument')
parser.add_argument('ppp', help='ppp help for default position argument')

parser.print_help()

