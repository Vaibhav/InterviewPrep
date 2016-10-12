import time

# terrible efficiency
# pretty sure its O(n!)

grids = [20,20]
 
def recPath(grid):
    # base case, no moves left
    if grid == [0,0]: return 1
    # recursive calls
    numofPaths = 0
    # move left when possible
    if grid[0] > 0:
        numofPaths += recPath([grid[0]-1,grid[1]])
    # move down when possible
    if grid[1] > 0:
        numofPaths += recPath([grid[0],grid[1]-1])
    return numofPaths
 
start = time.time()
result = recPath(grids)
elapsed = time.time() - start
 
print "result %s found in %s seconds" % (result, elapsed)