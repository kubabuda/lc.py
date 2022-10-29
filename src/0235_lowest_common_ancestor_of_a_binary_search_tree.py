from typing import *
import collections
from math import inf
import heapq
# 235. Lowest Common Ancestor of a Binary Search Tree
# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return f"TreeNode {self.val}{f' l:({self.left})' if self.left else ''}{f' r:({self.right})' if self.right else ''}"

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        i = 1
   

from unittest import TestCase
import unittest
import collections

null = None
class SolutionTests(unittest.TestCase):
    
    param_list = [
        ([6,2,8,0,4,7,9,null,null,3,5], 2, 8, 6),
    ]

    def testCases_lowestCommonAncestor(self):
        for nums, p, q, expected in self.param_list:
            with self.subTest():
                # arrange
                sol = Solution()
                root = buildTree(nums)
                pnode, qnode = getNode(root, p), getNode(root, q)
                print(p, pnode)
                print(q, qnode)
                # act
                result = sol.lowestCommonAncestor(root, p, q)
                # assert
                self.assertEqual(expected, result, (root, p, q))


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

def getNode(root: Optional[TreeNode], value: int) -> Optional[TreeNode]:
    if not root: 
        return None
    elif root.val > value: 
        return getNode(root.left, value)
    elif root.val == value:
        return root
    elif root.val < value: 
        return getNode(root.right, value)

if __name__ == '__main__':
    unittest.main()
