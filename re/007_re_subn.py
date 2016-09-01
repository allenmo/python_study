# -*- coding: utf-8 -*-

import re
'''
re.subn(pattern, repl, string[, count])
返回 (sub(repl, string[, count]), 替换次数)。
'''

pattern = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'

print re.subn(pattern, r'\2 \1',s)

def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()

print re.subn(pattern, func, s, 1)

### output ###
# ('say i, world hello!', 2)
# ('I Say, hello world!', 1)


