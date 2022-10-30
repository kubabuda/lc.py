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
        """one big min heap approach
        O(n*k*log (k*n))time, O(k*n) space"""
        result = None
        r_tail = None
        
        minheap = []
        for node in lists:
            while node:
                heapq.heappush(minheap, (node.val, id(node), node)) # added id so ListNode comparison wont be used for duplicated values
                node = node.next
                
        while minheap:
            val, _obj_id, to_add = heapq.heappop(minheap)
            if not result:
                result = to_add
                r_tail = result
            else:
                r_tail.next = to_add
                r_tail = r_tail.next
        return result

    def mergeKLists2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """bruteforce approach
        O(n*k*log (k*n))time, O(k*n) space"""
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

    def mergeKLists3(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """small min heap approach
        O(n*k*log k)time, O(k) space"""
        result = None
        r_tail = None
        
        minheap = []
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(minheap, (node.val, i, node))
                
        while minheap:
            val, i, to_add = heapq.heappop(minheap)
            if to_add.next:
                ne = to_add.next
                heapq.heappush(minheap, (ne.val, i, ne))
            if not result:
                result = to_add
                r_tail = result
            else:
                r_tail.next = to_add
                r_tail = r_tail.next

        return result
    
    def mergeKLists4(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """tree of merge 2 lists
        O(n*k*log k)time, O(k) space"""        
        if not lists: return None        

        def merge2Lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
            head = tail = None
            while list1 or list2:
                if list1 and (not list2 or list1.val <= list2.val):
                    to_add = list1
                    list1 = list1.next
                else:
                    to_add = list2
                    list2 = list2.next
                if not head:
                    head = to_add
                    tail = head
                else:
                    tail.next = to_add
                    tail = tail.next
            return head

        while len(lists) > 1:
            merged = []
            i = 0
            while i < len(lists):
                if i + 1 < len(lists):
                    m = merge2Lists(lists[i], lists[i + 1])
                    merged.append(m)
                    i += 1
                else:
                    merged.append(lists[i])
                i += 1
            lists = merged
        return lists[0]



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

    def testCases_mergeKLists3(self):
        for nums, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                lists = [ LoadListNode(n) for n in nums ]
                # act
                result = s.mergeKLists3(lists)
                # assert
                self.assertEqual(expected, ListNodeToArray(result), (nums))
    
    def testCases_mergeKLists4(self):
        for nums, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                lists = [ LoadListNode(n) for n in nums ]
                # act
                result = s.mergeKLists4(lists)
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
