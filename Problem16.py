# What is the sum of the digits of the number 2^1000?
import math

ans = 2 ** 1000
print ans
ans = str(ans)
len = len(ans)
sum = 0

for i in range(0,len):
    sum = int(ans[i]) + sum; 

print sum
