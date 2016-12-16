#!-_- coding;utf-8
'''
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.What is the smallest positive number
that is evenly divisible by all of the numbers from 1 to 20?
'''
num = 20
primes = [2]
primes2 = []
for x in range(3,num):
    for y in primes:
        if x % y == 0:
            break
    else:
        primes.append(x)
for n in primes:
    m = 2
    while n**m <= num:
        primes2.append(n)
        m += 1
primes.extend(primes2)
print(primes)
i = primes[0]*primes[1]
for x in range(2,len(primes)):
    i = i*primes[x]
print(i)


