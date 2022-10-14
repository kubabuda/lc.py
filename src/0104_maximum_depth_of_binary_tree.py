from typing import *
# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return f"TreeNode {self.val}{f' l:({self.left})' if self.left else ''}{f' r:({self.right})' if self.right else ''}"

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return 3


from unittest import TestCase
import unittest
import collections

null = None
class SolutionTests(unittest.TestCase):
    
    param_list = [
        ([3,9,20,null,null,15,7], 3),
        ([1,null,2], 2),
    ]

    def testCases_maxDepth(self):
        for nums, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                root = buildTree(nums)
                # act
                result = s.maxDepth(root)
                # assert
                self.assertEqual(expected, result, (nums, root))

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
