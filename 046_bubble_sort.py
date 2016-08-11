import argparse

parser = argparse.ArgumentParser('BubbleShort')
parser.add_argument('nums', nargs='+', type=int)
args = parser.parse_args()
print args.nums

length = len(args.nums)
i= length
for i in xrange(0, length-1):
    for j in xrange(0, length-1-i):
        if args.nums[j] > args.nums[j+1]:
            temp = args.nums[j]
            args.nums[j] = args.nums[j+1]
            args.nums[j+1] = temp

print args.nums
