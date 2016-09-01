# -*- coding: utf-8 -*-

import re
'''
re.sub(pattern, repl, string[, count])
使用repl替换tring中每一个匹配的子串后返回替换后的字符串。
'''

pattern = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'

print re.sub(pattern, r'\2 \1',s)

def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()

print re.sub(pattern, func, s, 1)

### output ###
# say i, world hello!
# I Say, hello world!

