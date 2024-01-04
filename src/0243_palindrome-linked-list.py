from typing import *
from linkedlist import ListNode
# 234. Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []
        curr = head
        while curr != None:
            values.append(curr.val)
            curr = curr.next
        cnt = len(values) // 2
        lastVal = len(values) - 1
        curr = head
        for i in range(cnt):
            if values[lastVal - i] != curr.val:
                return False
            curr = curr.next
        return True


import unittest
from linkedlist import *
null = None
class SolutionTests(unittest.TestCase): 
    param_list = lambda _:[
        ([1,2,2,1], True),
        ([1,2,1], True),
        ([1,2,3,1], False),
        ([1,2], False),
    ]

    def testCases_isPalindrome(self):
        for nums, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                head = LoadListNode(nums)
                # act
                result = s.isPalindrome(head)
                # assert
                self.assertEqual(expected, result, (nums))


if __name__ == '__main__':
    unittest.main()
