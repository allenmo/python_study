import argparse

parser=argparse.ArgumentParser()
parser.add_argument('-bacon')
parser.add_argument('-badger')
print parser.parse_args('-bac MMM'.split())
print parser.parse_args('-bad kkk'.split())
print parser.parse_args('-ba hhh'.split())
