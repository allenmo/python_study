import time

def isPrime(n):
    if n==2 or n ==3: return True
    if n%2==0 or n<2: 
        print '\t', 2
        return False
    for i in range(3, int(n**0.5)+1, 2):   #only odd numbers
        if n%i == 0: 
            print '\t', i
            return False
    return True

def is_prime(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: 
        print '\t', 2
        return False
    if n<9: return True
    if n%3 == 0: 
        print '\t', 3
        return False
    r = int(n**0.5)
    f = 5
    while f <= r:
        #print '\t', f
        if n%f == 0: 
            print '\t', f
            return False
        if n%(f+2) == 0: 
            print '\t', f+2
            return False
        f +=6
    return True

n = int(input('Input a number to check if prime:'))
t1 = float(time.time())
while n != None:
    #if isPrime(n):
    if is_prime(n):
        print "It is a prime"
    else:
        print "Not a prime" 
    t2 = float(time.time())
    print int(t2-t1), "s used."
    n = int(input('Input a number to check if prime:'))
    t1 = float(time.time())
