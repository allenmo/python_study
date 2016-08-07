import argparse

parser=argparse.ArgumentParser(prog='game.py')
parser.add_argument('move', choices=['rock', 'paper', 'scissors'])
print parser.parse_args(['rock'])

print parser.parse_args(['fire'])

