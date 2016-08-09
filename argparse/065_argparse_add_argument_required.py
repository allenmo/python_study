import argparse

parser=argparse.ArgumentParser()
parser.add_argument('--foo', required=True)
print parser.parse_args(['--foo', 'BAR'])

print parser.parse_args([])
