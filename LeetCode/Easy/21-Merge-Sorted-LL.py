'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        lst1 = l1
        lst2 = l2
        lst3 = ListNode(-1)
        tmp = lst3
        
        while lst1 is not None or lst2 is not None:
            if lst1 and lst2 and lst1.val < lst2.val:
                lst3.next = ListNode(lst1.val)
                lst1 = lst1.next
            elif lst2 and lst1 and lst2.val <= lst1.val: 
                lst3.next = ListNode(lst2.val)
                lst2 = lst2.next
            elif lst1:
                lst3.next = lst1
                break
            else:
                lst3.next = lst2
                break
                
            lst3 = lst3.next
        
        return tmp.next