import argparse

#parser = argparse.ArgumentParser(prog='PROG')
parser = argparse.ArgumentParser()

parser.add_argument('--version','-v', action='version', version='%(prog)s 2.0')
parser.parse_args()
