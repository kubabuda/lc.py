from typing import *
# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list
import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next    

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next: return None # result can be empty
        tail = head
        pre = head
        i = 0
        while tail.next:
            tail = tail.next
            if i >= n:
                pre = pre.next
            i += 1
        if i == n - 1: # we are removing first element from list
            return head.next
        pre.next = pre.next.next

        return head


from unittest import TestCase
import unittest

class SolutionTests(unittest.TestCase): 

    param_list = [
        ([1,2,3,4,5], 2, [1,2,3,5]),
        ([0], 1, []),
        ([1,2], 1, [1]),
        ([1,2], 2, [2]),
    ]

    def testCases_removeNthFromEnd(self):
        for nums, k, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                head = LoadListNode(nums)
                # act
                result = s.removeNthFromEnd(head, k)
                # assert
                self.assertEqual(expected, ListNodeToArray(result), (nums, k))


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
