import argparse

parser=argparse.ArgumentParser()
parser.add_argument('--persantage', '-p', dest='p', type=float, default=3.25)
args=parser.parse_args()
print args
m0=10000
m=m0
n=0
while m < 2*m0:
    n=n+1
    m=m*(1 + args.p/100)
print n, "years later, money will double"
