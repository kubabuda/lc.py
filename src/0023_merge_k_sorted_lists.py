from typing import *
# 23. Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists
import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next    

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """one big min heap approach"""
        result = None
        r_tail = None
        
        minheap = []
        for node in lists:
            while node:
                heapq.heappush(minheap, node.val)
                node = node.next
                
        while minheap:
            val = heapq.heappop(minheap)
            to_add = ListNode(val=val)
            if not result:
                result = to_add
                r_tail = result
            else:
                r_tail.next = to_add
                r_tail = r_tail.next
        return result

    def mergeKLists2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """bruteforce approach"""
        result = None
        r_tail = None
        
        values = []
        for node in lists:
            while node:
                values.append(node)
                node = node.next
        values.sort(key=lambda n: n.val)
                
        for to_add in values:
            if not result:
                result = to_add
                r_tail = result
            else:
                r_tail.next = to_add
                r_tail = r_tail.next
        return result


from unittest import TestCase
import unittest

class SolutionTests(unittest.TestCase): 

    param_list = [
        ([[1,2,4], [1,3,4]], [1,1,2,3,4,4]),
        ([], []),
        ([[], [0]], [0]),
    ]

    def testCases_mergeKLists(self):
        for nums, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                lists = [ LoadListNode(n) for n in nums ]
                # act
                result = s.mergeKLists(lists)
                # assert
                self.assertEqual(expected, ListNodeToArray(result), (nums))

    def testCases_mergeKLists2(self):
        for nums, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                lists = [ LoadListNode(n) for n in nums ]
                # act
                result = s.mergeKLists2(lists)
                # assert
                self.assertEqual(expected, ListNodeToArray(result), (nums))


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
