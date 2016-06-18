

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#worked out prime facotrization
num = 1*2*3*5*7*11*13*17*19*2*2*3*2
print "LCM: " + str(num);


# used brute force to check for LCM(1, range(1,21))
# cut down some conditionals by eliminating thm if two other factors were multiplied to create them.
x = 10000
while(1):
    if ((x % 5 == 0) and (x % 7 == 0) and (x % 9 == 0) and (x % 11 == 0) and (x % 12 == 0)
        and (x % 13 == 0) and (x % 16 == 0) and (x % 17 == 0) and (x % 19 == 0)):
        print "LCM of all the numbers between 1 and 20: " + str(x)
        break;
    else:
        # has to be even so able to increment by 2
        # obviously a large number so starting at higher number than given (2520)
        x = x + 2

#232792560
