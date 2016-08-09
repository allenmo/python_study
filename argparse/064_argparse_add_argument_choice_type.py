import argparse

parser=argparse.ArgumentParser(prog='doors.py')
parser.add_argument('door', type=int, choices=range(1,4)) # type conversion first, then in choices container check
print parser.parse_args(['3'])
print parser.parse_args(['4'])
