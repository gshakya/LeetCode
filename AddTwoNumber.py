'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807. 

https://leetcode.com/problems/add-two-numbers/

'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

l1_1 = ListNode(1)
l1_2 = ListNode(8)

l1_1.next = l1_2
# l1_2.next= l1_3
        
        
        
l2_1 = ListNode(0)
# l2_2 = ListNode(6)
# l2_3 = ListNode(7)

# l2_1.next = l2_2
# l2_2.next= l2_3     
        
        
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while (l1 is not None or l2 is not None):
            val1 =  0 if l1 is None else l1.val  
            val2 =  0 if l2 is None else l2.val
            sum = val1+val2+carry
            carry = sum//10
            curr.next = ListNode(sum%10)                     
            curr = curr.next
            l1 = None if l1 is None else l1.next
            l2 = None if l2 is None else l2.next
            
            if (carry > 0):
                curr.next = ListNode(carry)
        return dummyHead.next

        
s1 = Solution()
result = s1.addTwoNumbers(l1_1,l2_1)

print(result)