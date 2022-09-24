from typing import *
# 23. Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next    

class Solution:
    def mergeTwoLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        result = None
        r_tail = None
        tails = [l for l in lists if l]
        while tails:
            i_min = 0
            for i, t in enumerate(tails):
                if t.val < tails[i_min].val:
                    i_min = i
            to_add = tails[i_min]
            if not to_add.next:
                tails.remove(to_add)
            else:
                tails[i_min] = to_add.next
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

    def testCases_mergeTwoLists(self):
        for nums, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                lists = [ LoadListNode(n) for n in nums ]
                # act
                result = s.mergeTwoLists(lists)
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
