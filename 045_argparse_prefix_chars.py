import argparse

parser = argparse.ArgumentParser(prog='PROG', prefix_chars='-+', add_help=False)

parser.add_argument('+f')
parser.add_argument('++bar')
args = parser.parse_args('+f X ++bar Y'.split())
print args

#parser.add_argument('-f')
#parser.add_argument('--foo')
#args2 = parser.parse_args('-f X --foo Y'.split())
#print args2
