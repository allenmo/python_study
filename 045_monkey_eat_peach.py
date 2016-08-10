def cal_before(last):
    before=(last+1) * 2
    return before

last=1
for i in xrange(0,10):
    before=cal_before(last)
    last=before

print before
