import argparse

parser=argparse.ArgumentParser()
parser.add_argument('--foo') # optional parameter use upper case FOO for metavar
parser.add_argument('bar') # position parameter use itself for metavar
parser.parse_args('X --foo Y'.split())
#parser.print_help()

parser.add_argument('-x', nargs=2)
parser.add_argument('--koo', nargs=2, metavar=('bar', 'baz'))

parser.print_help()
