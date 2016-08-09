import argparse

parser = argparse.ArgumentParser(
        prog='prog',
        description='''this description
            was indeted weird
                but that is okay''',
        epilog='''
            likewise for this epilog whose whitespace will
            be cleaned up and whose words will be wrapped
            accross a couple lines''')
parser.print_help()

