from typing import *
# 21. Merge Two Sorted Lists
# https://leetcode.com/problems/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next    

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = None
        tail = None
        while list1 or list2:
            to_add = None
            if list1 and (not list2 or list1.val <= list2.val):
                to_add = list1
                list1 = list1.next
            else:
                to_add = list2
                list2 = list2.next
            
            if not result:
                result = to_add
                tail = result
            else:
                tail.next = to_add
                tail = tail.next
        return result


from unittest import TestCase
import unittest

class SolutionTests(unittest.TestCase): 

    param_list = [
        ([1,2,4], [1,3,4], [1,1,2,3,4,4]),
        ([], [], []),
        ([], [0], [0]),
    ]

    def testCases_mergeTwoLists(self):
        for nums1, nums2, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                head1 = LoadListNode(nums1)
                head2 = LoadListNode(nums2)
                # act
                result = s.mergeTwoLists(head1, head2)
                # assert
                self.assertEqual(expected, ListNodeToArray(result), (nums1, nums2))


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
