# sieve of Eratosthenes, prime factorization algo
maxx = max(nums) + 1
primes = [True] * maxx
p = 2
while p*p < maxx:
    if primes[p]:
        for i in range(p*p, maxx, p):
            primes[i] = False
    p += 1