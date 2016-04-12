#!/usr/bin/python3

import re

s="Are you afraid of ghosts?"
flag = "ghosts" in s
print(flag)
print("ghosts" in s)
print(("ghosts" in s))
print("the result is ", ("ghosts" in s))
print("the result is ", "ghosts" in s)
print("coffee not in s", "coffee" not in s)
print("coffee in s", "coffee" in s)


ss="123"
matcher = re.match('\d{3}\Z',ss)

if matcher:
	print("True!")
else:
	print("False!")
print(re.match('\d{4}\Z',ss))
print(matcher)

sss="a2bc"
print(re.match('\w\d',sss))
matcher = re.match('\*\d\Z',sss)
