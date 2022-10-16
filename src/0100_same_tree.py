from typing import *
import collections
# 100. Same Tree
# https://leetcode.com/problems/same-tree/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return f"TreeNode {self.val}{f' l:({self.left})' if self.left else ''}{f' r:({self.right})' if self.right else ''}"

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        if not p or not q or p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        

from unittest import TestCase
import unittest
import collections

null = None
class SolutionTests(unittest.TestCase):
    
    param_list = [
        ([1,2,3], [1,2,3], True),
        ([1,2,1], [1,2,2], False),
    ]

    def testCases_isSameTree(self):
        for numsp, numsq, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                p, q = buildTree(numsp), buildTree(numsq)
                # act
                result = s.isSameTree(p, q)
                # assert
                self.assertEqual(expected, result, (numsp, numsq, p, q))


def buildTree(nums: List[int]) -> Optional[TreeNode]:
    queue = collections.deque()
    result = None
    for i, val in enumerate(nums):
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
