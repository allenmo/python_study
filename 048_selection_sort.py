import argparse

parser=argparse.ArgumentParser()
parser.add_argument('nums', nargs='+', type=int)
args=parser.parse_args()

def selectionSort(List):
    exchanges_count = 0
    for i in xrange(0,len(List)):
        min = i
        for j in xrange(i+1, len(List)):
            if List[min] > List[j]:
                min = j
        if min != i:
            List[min], List[i] = List[i], List[min]
            exchanges_count += 1
    print 'exchanges for: ', exchanges_count, ' times'
    return List

print selectionSort(args.nums)

