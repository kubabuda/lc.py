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
        """O(n) space O(n) time"""
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
            tail = tail.next
            i += 1

    def reorderList2(self, head: Optional[ListNode]):
        """O(1) space O(n) time"""
        tail = head
        n = 0
        while tail:
            tail = tail.next
            n += 1          # count nodes in input
    
        def reverseLL(node, prev=None):
            if not node: return prev
            ne = node.next
            node.next = prev
            return reverseLL(ne, node)
    
        skip = int(n / 2)
        if n % 2: skip += 1
        rhead = None        # after half of input
        i = 1               # reverse second half
        tail = head
        while i < skip:
            tail = tail.next
            i += 1
        
        rhead = reverseLL(tail.next)
        tail.next = None    # cutoff reversed half from original
        result = head       # start from original head
        head = head.next
        tail = result
        while head or rhead:
            if rhead:       # add one from end (reversed head)
                tail.next = rhead
                rhead = rhead.next
                tail = tail.next
            if head:        # add one from original head
                tail.next = head
                head = head.next
                tail = tail.next


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

    def testCases_reorderList2(self):
        for nums, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                head = LoadListNode(nums)
                # act
                s.reorderList2(head)
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
