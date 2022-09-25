from typing import *
# 143. Reorder List
# https://leetcode.com/problems/reorder-list
import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next    

    def __repr__(self):return f'Node val={self.val} [next={self.next}]'

import collections
class Solution:
    def reorderList(self, head: Optional[ListNode]):
        nodes = collections.deque()
        tail = head.next
        while tail:
            curr = tail
            tail = tail.next
            curr.next = None # whyy is it needed
            nodes.append(curr)
        i = 0
        tail = head
        while nodes:
            if i % 2:
                curr = nodes.popleft()
            else: 
                curr = nodes.pop()
            tail.next = curr
            tail = curr
            i += 1


from unittest import TestCase
import unittest

class SolutionTests(unittest.TestCase): 

    param_list = [
        ([1,2,3,4], [1,4,2,3]),
        ([1,2,3,4,5], [1,5,2,4,3]),
    ]

    def testCases_reorderList(self):
        for nums, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                head = LoadListNode(nums)
                # act
                s.reorderList(head)
                # assert
                self.assertEqual(expected, ListNodeToArray(head), (nums))


def LoadListNode(arr):
    head = None
    for n in arr[::-1]:
        head = ListNode(n, head)
    return head

def ListNodeToArray(node, arr=None):
    if not arr: arr = []
    if node:
        arr.append(node.val)
        if node.next: ListNodeToArray(node.next, arr)
    return arr

if __name__ == '__main__':
    unittest.main()
