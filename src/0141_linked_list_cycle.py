from typing import *
# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next    

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        curr = head
        while curr:
            if curr in visited: return True
            visited.add(curr)
            curr = curr.next
        return False


from unittest import TestCase
import unittest

class SolutionTests(unittest.TestCase): 

    param_list = [
        ([], -1, False),
        ([1,2,3], -1, False),
        ([1,2,3,4,5], 2, True),
        ([3,2,0,-4], -1, False),
        ([-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5], -1, False),
        ([-21,10,17,8,4,26,5,35,33,-7,-16,27,-12,6,29,-12,5,9,20,14,14,2,13,-24,21,23,-21,5], 12, True),
    ]

    def testCases_hasCycle(self):
        for nums, i, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                head = LoadListNode(nums)
                if i >= 0:
                    tail = head
                    while tail.next:
                        tail = tail.next
                    tailNext = head
                    for _ in range(i):
                        if tailNext.next:
                            tailNext = tailNext.next
                    tail.next = tailNext
                # act
                result = s.hasCycle(head)
                # assert
                self.assertEqual(expected, result, (nums, i))

def LoadListNode(arr):
    head = None
    for n in arr[::-1]:
        head = ListNode(n, head)
    return head

if __name__ == '__main__':
    unittest.main()
