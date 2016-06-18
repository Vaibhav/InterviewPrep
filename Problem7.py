

n = 10001
primes = [2, 3, 5, 7, 11]

def is_prime(num):
    prime_status = 1;
    for i in range(0, len(primes), 1):

        if (primes[i] > (num ** (0.5))):
            return prime_status;
        if (num % primes[i] == 0):
            prime_status = 0;

p = 12;

while(1):
    if len(primes) >= n+1:
        break;
    if is_prime(p):
        print p
        primes.append(p);
    p = p + 1;

print "The 10 001st prime is: " + str(primes[n-1]);

