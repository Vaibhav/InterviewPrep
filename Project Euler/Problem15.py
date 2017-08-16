
import time

start = time.time()


def factorial(num):
    f = 1
    for x in xrange(1, num + 1):
        f = f * x
    return f

n = 40      # The total number of moves for any one path (right + down)
r = 20      # The total number of right moves for any one path

ans = (factorial(n) / factorial(r) / factorial(r))

print "Answer: " + str(ans)
end = time.time() - start
print end

# 0.00100016593933 seconds
