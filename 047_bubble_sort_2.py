import argparse

parser = argparse.ArgumentParser('BubbleShort')
parser.add_argument('nums', nargs='+', type=int)
args = parser.parse_args()
print args.nums

def bobbleSort(List):
    for i in xrange(len(List)-1, 0, -1):
        for j in xrange(0, i):
            if List[j] > List[j+1]:
                List[j], List[j+1] = List[j+1],List[j]
    return List

print bobbleSort(args.nums)
