
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
