natural = list(x for x in range(1000))
sieve = list(x for x in natural if x%3 ==0 or x % 5==0)

print(sum(sieve))

