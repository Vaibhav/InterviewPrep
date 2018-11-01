'''
Input: 1->1->2->3->3
Output: 1->2->3
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, node):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if node is None:
            return node
        
        head = node 
        
        while head.next is not None: 
            
            if head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
        
        return node