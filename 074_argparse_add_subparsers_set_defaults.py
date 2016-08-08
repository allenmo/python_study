import argparse

def foo(args):
    print args.x * args.y

def bar(args):
    print '((%s))' % args.z

parser=argparse.ArgumentParser()
subparsers=parser.add_subparsers()

# create the parser for the 'foo' command
parser_foo=subparsers.add_parser('foo')
parser_foo.add_argument('-x', type=int, default=1)
parser_foo.add_argument('y', type=float)
parser_foo.set_defaults(func=foo)

args=parser.parse_args('foo 1 -x 2'.split())
args.func(args) # call whatever function was selected

# create the parser for the 'bar' command
parser_bar=subparsers.add_parser('bar')
parser_bar.add_argument('z')
parser_bar.set_defaults(funcc=bar)
args=parser.parse_args('bar kkkkk'.split())
args.funcc(args) # call whatever function was selected





