from typing import *
# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def toArray(self, arr=None):
        if not arr: arr = []
        arr.append(self.val)
        if self.next: self.next.toArray(arr)
        return arr

    def __str__(self):
        return f"LNode {self.val},ne={self.next}"

    @classmethod
    def load(cls, arr):
        head = None
        for n in arr[::-1]:
            head = ListNode(n, head)
        return head
    

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev

from unittest import TestCase
import unittest

class SolutionTests(unittest.TestCase): 

    param_list = [
        ([1,2,3], [3,2,1]),
        ([1,2,3,4,5], [5,4,3,2,1]),
    ]

    def testCases_reverseList(self):
        for nums, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                ll = ListNode.load(nums)
                # act
                result = s.reverseList(ll)
                # assert
                self.assertEqual(expected, result.toArray(), (nums))


if __name__ == '__main__':
    unittest.main()
