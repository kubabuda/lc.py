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
            nodes.append(tail)
            tail = tail.next
            nodes[-1].next = None   # needed so last element doesnt introduce cycle

        tail = head
        while nodes:
            tail.next = nodes.pop()
            tail = tail.next
            if nodes:
                tail.next = nodes.popleft()
                tail = tail.next

    def reorderList2(self, head: Optional[ListNode]):
        """O(1) space O(n) time"""
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        rhead = slow.next   # find midpoint of linked list
        prev = slow.next = None
    
        while rhead:        # reverse second half of linked list 
            temp = rhead.next
            rhead.next = prev
            prev = rhead
            rhead = temp
        rhead = prev

        result = tail = head # start from original head
        head = head.next    # skip node already in result 
        while head or rhead:
            if rhead:       # add one from end (reversed head)
                tail.next = rhead
                rhead = rhead.next
                tail = tail.next
            if head:        # add one from beginning
                tail.next = head
                head = head.next
                tail = tail.next


from unittest import TestCase
import unittest

class SolutionTests(unittest.TestCase): 

    param_list = [
        ([1], [1]),
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
