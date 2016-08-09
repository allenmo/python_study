import argparse

parser=argparse.ArgumentParser()
parser.add_argument('-f')
parser.add_argument('bar')
print parser.parse_args('-- -f'.split()) # -- here is presdo-aprgment tell parse_args() that, all aprgument after -- is positional argument
