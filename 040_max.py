import argparse

parser=argparse.ArgumentParser('max')
parser.add_argument('x', type=float)
parser.add_argument('y', type=float)
args=parser.parse_args()

if args.x != None and args.y != None:
    if args.x >= args.y:
        print args.x
    else:
        print args.y
