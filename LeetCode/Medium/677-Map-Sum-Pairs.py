'''
Implement a MapSum class with insert, and sum methods.

For the method insert, you'll be given a pair of (string, integer). The string represents the key and the integer represents the value. If the key already existed, then the original key-value pair will be overridden to the new one.

For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the pairs' value whose key starts with the prefix.
'''


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.theMap = {}
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.theMap[key] = val;
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        sum = 0; 
        for i in self.theMap.keys():
            if i.startswith(prefix):
                sum += self.theMap[i]
        return sum


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
