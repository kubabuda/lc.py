from typing import *
# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next    

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
                head = LoadListNode(nums)
                # act
                result = s.reverseList(head)
                # assert
                self.assertEqual(expected, ListNodeToArray(result), (nums))

def LoadListNode(arr):
    head = None
    for n in arr[::-1]:
        head = ListNode(n, head)
    return head

def ListNodeToArray(node, arr=None):
    if not arr: arr = []
    arr.append(node.val)
    if node.next: ListNodeToArray(node.next, arr)
    return arr

if __name__ == '__main__':
    unittest.main()
