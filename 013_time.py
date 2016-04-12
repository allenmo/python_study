#!/usr/bin/python3

import time

content = dir(time)
print(content)

ticks = time.time()
print("Ticks since epoch: ", ticks)

timenow = time.localtime(time.time())
print("Current local time: ", timenow)

print("Year: ", timenow[0])
print("Month: ", timenow[1])
print("Day: ", timenow[2])

asctime = time.asctime(time.localtime(time.time()))
print(asctime)
