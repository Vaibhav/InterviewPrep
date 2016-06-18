
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

num = 600851475143
largest = 1
x = 1

def is_prime(n):
	if n % 2 == 0:
		return 0;
	i = 3
	while (i < n/2):
		if (n%i  == 0):
			return  0;
		
		i = i + 2
	
	return 1;
	
	
	
while x < 10000:
        if x <= 0:
                break;

        if(num % x == 0):

                if(is_prime(x)) and (x > largest):
                        largest = x;
                        
        print x
        x = x + 2
		
print "Largest Prime is: "
print largest

# 6857
