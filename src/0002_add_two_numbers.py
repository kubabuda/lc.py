from typing import *

# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1, None)
        tail = head
        carry = 0

        while l1 or l2 or carry:
            curr = carry
            carry = 0
            if l1:
                curr += l1.val
                l1 = l1.next
            if l2:
                curr += l2.val
                l2 = l2.next
            if curr >= 10:
                carry = curr // 10
                curr %= 10
            
            tail.val = curr
            if l1 or l2 or carry:
                tail.next = ListNode(-1, None)
                tail = tail.next

        return head


import unittest
from linkedlist import *

class SolutionTests(unittest.TestCase): 
    
    param_list = lambda _: [
        (LoadListNode([2, 4, 3]), LoadListNode([5, 6, 4]), [7, 0, 8]),
    ]

    def testCases_addTwoNumbers(self):
        for l1, l2, expected in self.param_list():
            with self.subTest():
                # arrange
                sol = Solution()
                # act
                result = sol.addTwoNumbers(l1, l2)
                # assert
                self.assertEqual(ListNodeToArray(result), expected, f'{l1}, {l2}: {result} != {expected}')


if __name__ == '__main__':
    unittest.main()
