#!/usr/bin/python
import re

x = """
name: Charles
Address: BUPT

name: Ann
Address: BUPT
"""
p = re.compile(r"^name:(.*)\n^Address:(.*)\n", re.M)
#p = re.compile(r"^name:(?P.*)\n^Address:(?P.*)\n", re.M)
for m in p.finditer(x):
    print m.span()
    print "here is your friends list"
    print "%s, %s"%m.groups()

