import argparse

parser=argparse.ArgumentParser(prog='frobble')
parser.add_argument('--foo', action='store_true', help='foo the bars before frobbling')
parser.add_argument('bar', nargs='+', help='one of the bars to be frobbled')
#print parser.parse_args('-h'.split())

parser.add_argument('specifier', nargs='?', type=int, default=42,
        help='the specifier to %(prog)s (default: %(default)s)')

parser.add_argument('--hideHelp', help=argparse.SUPPRESS)

parser.print_help()

