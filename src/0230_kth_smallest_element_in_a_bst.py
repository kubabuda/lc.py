from typing import *
import collections
from math import inf
import heapq
# 230. Kth Smallest Element in a BST
# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return f"TreeNode {self.val}{f' l:({self.left})' if self.left else ''}{f' r:({self.right})' if self.right else ''}"
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        minheap = []

        def dfs(node):
            if len(minheap) < k or minheap[0] < -node.val:
                heapq.heappush(minheap, -node.val)
            while len(minheap) > k:
                heapq.heappop(minheap)
            if node.left: dfs(node.left)
            if node.right: dfs(node.right)
        
        dfs(root)
        return -minheap[0]

    def kthSmallest2(self, root: Optional[TreeNode], k: int) -> int:
        i = 1

        def dfs(node):
            nonlocal i
            if not node: return None
            if node.left: 
                l = dfs(node.left)
                if l is not None: return l
            if i == k: return node.val
            i += 1
            if node.right:
                r = dfs(node.right)
                if r is not None: return r
            return None
        
        return dfs(root)


from unittest import TestCase
import unittest
import collections

null = None
class SolutionTests(unittest.TestCase):
    
    param_list = [
        ([4,2,6,1,3,5,7], 4, 4),
        ([4,2,6,1,3,5,7], 3, 3),
        ([3,1,4,null,2], 1, 1)
    ]

    def testCases_kthSmallest(self):
        for nums, k, expected in self.param_list:
            with self.subTest():
                # arrange
                sol = Solution()
                root = buildTree(nums)
                # act
                result = sol.kthSmallest(root, k)
                # assert
                self.assertEqual(expected, result, (root, k))

    def testCases_kthSmallest2(self):
        for nums, k, expected in self.param_list:
            with self.subTest():
                # arrange
                sol = Solution()
                root = buildTree(nums)
                # act
                result = sol.kthSmallest2(root, k)
                # assert
                self.assertEqual(expected, result, (root, k))


def buildTree(numsBFS: List[int]) -> Optional[TreeNode]:
    queue = collections.deque()
    result = None
    for i, val in enumerate(numsBFS):
        node = None
        if val != None:
            node = TreeNode(val)
            queue.append(node)
        if not result:
            result = node
        else:
            if i & 1:
                queue[0].left = node
            else:
                queue[0].right = node
                queue.popleft()
    return result


if __name__ == '__main__':
    unittest.main()
