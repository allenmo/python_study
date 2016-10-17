import md5, binascii

with open('0.bin', 'rb') as f:
    s = md5.new(f.read()).hexdigest()
with open('2BIT_PANEL.bin', 'rb') as ff:
    ss = md5.new(ff.read()).hexdigest()
print  s,repr(s), len(s)
print ss, repr(ss), len(ss)

with open('2BIT_PANEL.bin', 'rb') as fff:
    sss = binascii.crc32(fff.read()) & 0xFFFFFFFF
print sss, hex(sss),  hex(int(sss)), hex(int(sss)).upper(), hex(long(0))

