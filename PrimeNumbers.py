import math
import time
import os
import winsound
end = 1

while end != 0:
    primes = []
    end = int(input("How many prime numbers: "))
    os.system('cls')
    primeCounter = 1

    t1 = time.time()
    while len(primes) < end:
        primeCounter += 2
        isPrime = True

        for primeCounter2 in range(2, math.floor(math.sqrt(primeCounter)) + 1):
            if primeCounter % primeCounter2 == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(primeCounter)

    primes.insert(0, 2)
    t2 = time.time()

    print(primes)
    print(round(t2 - t1, 3))

   

    
