#!/usr/bin/python3

filename = "readme.txt"

with open(filename) as fn:
	content = fn.readlines()
print(content)
fn.close()

f = open("output.txt","w")
f.write("Pythonprogramminglanguage.com, \n")
f.write("Example program.")
f.close()

