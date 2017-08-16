def divisors(n):
    i = 1
    d = 0
    while i*i <= n:
        if n % i == 0:
            d += 1
        i += 1
    return d * 2

i = 1
t = 1
while divisors(t) <= 500:
    i += 1
    t += i


print t
print "Number of Divisors = ", divisors(t)
