'''
 You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

Example 1:

Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".

Example 2:

Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).

'''


class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        
        dic = {}
        
        for i,v in enumerate(list1):
            dic[v] = i
            
            
        min_sum = len(list2) + len(list1) + 1
        minResto = None
        
        for i,v in enumerate(list2):
            if v in dic:
                if dic[v] + i < min_sum:
                    minResto = [v]
                    min_sum = i + dic[v]
                elif dic[v] + i == min_sum:
                    minResto.append(v)
        return minResto