# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        def create(l, l1, l2, carry):
            if (l1 is None and l2 is None) and carry >= 1:
                l.next = ListNode(carry)
                return
            elif l1 is None and l2 is None:
                return
            elif l1 is None and l2 is not None:
                l1 = ListNode(0)
            elif l2 is None and l1 is not None: 
                l2 = ListNode(0)
            l.next = ListNode((carry + l1.val + l2.val) % 10)
            carry = (carry + l1.val + l2.val) / 10
            return create(l.next, l1.next, l2.next, carry)
        
        ret = ListNode((l1.val + l2.val) % 10)
        carry = (l1.val + l2.val) / 10
        
        create(ret, l1.next, l2.next, carry)
        
        return ret
        
                
