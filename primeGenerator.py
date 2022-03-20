"""
Used to generate two adequately large strong pseudo-primes using the Rabin-Miller Primality Test
"""
import random

#generate list of primes less than 1000 using Eratosthene's Sieve
PRIMES_LT_1000 = []
x = [0, 0] + list(range(2, 1001))
for num in x:
    if num:
        for y in range(2, 1000//num + 1):
            x[num * y] = 0
        PRIMES_LT_1000.append(num)

#check if a number has a factor from the list of primes less than 1000
#params: int num
##num: potential prime candidate
#return: True if number has a small factor and therefore is composite
##False otherwise
def has_small_factor(num):
    for x in PRIMES_LT_1000:
        if num % x == 0:
            return True
    return False

#run rabin miller test on num specified number of times
#params: int num, int runs
##num: the number to be tested
##runs: how many times to run the test, more runs indicates better probability the test is accurate
#return True if passes Rabin Miller which indicates the number is a strong pseudoprime
##False otherwise indicating number is not prime
def rabin_miller_test(num, runs):
    #print('rm')
    #write num - 1 as 2**x * y
    x, y = 0, num-1
    while not(y & 1) and y > 0:
        y //= 2
        x += 1
    #print('past factorizing')
    for run in range(runs):
        a = random.randint(2, num-1)
        z = pow(a, y, num)
        if z==1 or z==num-1:
            continue
        for repeat in range(x - 1):
            z = pow(z, 2, num) #z ** 2 % num
            if z == num - 1:
                continue
        return False
    return True


#runs has_small_factor and rabin_miller_test on a potential prime number
#params: int potential_prime
##potential_prime: number to be tested
#return: True if strong pseudoprime; false otherwise
def test_number(potential_prime):

    if has_small_factor(potential_prime):
        #print('failed hsf')
        return False
    if rabin_miller_test(potential_prime, 10):
        return True
    return False
    #print('failed rmt')

#generates a large, strong pseudoprime using test number and randrange
#return: int value b/w 1024 and 4096 bits.
def get_prime():
    #first generate a random odd number b/w 1024 bits and 4096
    rprime = random.randrange(2**1024 + 1, 2**4096, 2)
    while not (test_number(rprime)):
        rprime = random.randrange(2**1024 + 1, 2**2048, 2)
        #print()
    return(rprime)

"""
a = get_prime()
b = get_prime()

print(a, b)
"""
