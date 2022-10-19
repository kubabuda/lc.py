from typing import *
import collections
import heapq
# 102. Binary Tree Level Order Traversal
# https://leetcode.com/problems/binary-tree-level-order-traversal
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return f"TreeNode {self.val}{f' l:({self.left})' if self.left else ''}{f' r:({self.right})' if self.right else ''}"

class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        toVisit = collections.deque([(root, 0)])
        result = []
        
        while toVisit:
            node, lvl = toVisit.popleft()
            if not node: continue
            while lvl >= len(result): result.append([])
            result[lvl].append(node.val)
            if node.left: toVisit.append((node.left, lvl + 1))
            if node.right: toVisit.append((node.right, lvl + 1))

        return result


from unittest import TestCase
import unittest
import collections

null = None
class SolutionTests(unittest.TestCase):
    
    param_list = [
        ([1,2,3], [[1], [2,3]]),
        ([3,9,20,null,null,15,7], [[3],[9,20],[15,7]]),
        ([1], [[1]]),
        ([], [])
    ]

    def testCases_levelOrder(self):
        for nums, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                root = buildTree(nums)
                # act
                result = s.levelOrder(root)
                # assert
                self.assertEqual(expected, result, (nums, root))


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
