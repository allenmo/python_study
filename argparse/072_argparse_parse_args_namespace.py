import argparse

parser=argparse.ArgumentParser()
parser.add_argument('--foo')
args=parser.parse_args(['--foo','BAR'])
print vars(args)

class C(object):
    pass

c=C()
parser.parse_args('--foo BARRRRRR'.split(), namespace=c) # assign attribute to already existing object
print c.foo
