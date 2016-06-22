

def collatz(n, counter):
	
	while n > 1: 
	
		if (n % 2 == 0):
			n = n / 2;
		else:
			n = 3*n + 1;
		counter = counter + 1
		
	return counter;
		
limit = 1000000
max_seq = [0, 0]
		
for i in range(0, limit):
	col = collatz(i, 0)
	
	if col > max_seq[1]:
		max_seq[0] = i;
		max_seq[1] = col;		

print max_seq		
