import argparse
parser = argparse.ArgumentParser(description="some information here")
parser.add_argument("echo", help="echo the string you use here")
parser.add_argument("x", help="int, output x ** 2 ", type=int)
parser.add_argument("-a", action="store_true")
args = parser.parse_args()
print args.echo
print args.x ** 2
