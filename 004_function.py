#!/usr/bin/python3
import math

def pythagoras(a,b):
    value = math.sqrt(a*a + b*b)
    print(value)


pythagoras(3,3)

def pythagoras2(a,b):
    value = math.sqrt(a*a + b*b)
    return value

result = pythagoras2(3,4)
print(result)

