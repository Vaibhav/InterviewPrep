
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def square_of_sum(x):
    sum1 = 0;
    for a in range(1,x+1, 1):
        sum1 = sum1 + a;
    return sum1 ** 2;

def sum_of_squares(x):
    sum2 = 0;
    for b in range(1, x+1, 1):
        c = b ** 2
        sum2 = sum2 + c;
    return sum2

print "Difference between sum of squares and squares of sum of first 100 numbers: "
print square_of_sum(100) - sum_of_squares(100)

#====================================
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

#====================================
