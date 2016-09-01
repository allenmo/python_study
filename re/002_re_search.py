# -*- coding: utf-8 -*-

#导入re模块
import re
import pprint

# 将正则表达式编译成Pattern对象
pattern = re.compile('world')
# 使用search()查找匹配的子串， 不存在能匹配的子串时将返回None
# 这个例子中使用match()无法成功匹配
match = re.search(pattern, 'hello world!')
if match:
    # 使用match获得分组信息
    print dir(match)
    print "---------------------------------------------------------"
    print "match.string:", match.string
    print "match.re:", match.re
    print "match.pos:", match.pos
    print "match.endpos:", match.endpos
    print "match.lastindex:", match.lastindex
    print "match.lastgroup:", match.lastgroup
    print "match.group():", match.group()
    print "match.group(0):", match.group(0)
    print "match.groups():", match.groups()
    print "match.groupdict():", match.groupdict()
    print "match.start(0):", match.start(0)
    print "match.end(0):", match.end(0)
    print "match.span(0):", match.span(0)
else:
    print "match:", match

### output ###
# ['__class__', '__copy__', '__deepcopy__', '__delattr__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'end', 'endpos', 'expand', 'group', 'groupdict', 'groups', 'lastgroup', 'lastindex', 'pos', 're', 'regs', 'span', 'start', 'string']
# ---------------------------------------------------------
# match.string: hello world!
# match.re: <_sre.SRE_Pattern object at 0x7f4c3b34bcb0>
# match.pos: 0
# match.endpos: 12
# match.lastindex: None
# match.lastgroup: None
# match.group(): world
# match.group(0): world
# match.groups(): ()
# match.groupdict(): {}
# match.start(0): 6
# match.end(0): 11
# match.span(0): (6, 11)

