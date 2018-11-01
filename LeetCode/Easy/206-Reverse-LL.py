# Reverse singly linked list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cur = head
        prev = None 
        
        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        cur = prev
        head = cur
        return head