from typing import *
import collections
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
        if not root: return 0
        maxH = 0
        toVisit = [(root, 1)]

        while toVisit:
            node, h = toVisit.pop()
            if node.left: toVisit.append((node.left, h + 1))
            if node.right: toVisit.append((node.right, h + 1))
            maxH = max(h, maxH)

        return maxH

    def maxDepthRec(self, root: Optional[TreeNode], h = 0) -> int:
        if not root: return 0
        return max(self.maxDepthRec(root.left), self.maxDepthRec(root.right)) + 1

    def maxDepthBFS(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        maxH = 0
        queue = collections.deque([(root, 1)])

        while queue:
            node, h = queue.popleft()
            if node.left: queue.append((node.left, h + 1))
            if node.right: queue.append((node.right, h + 1))
            maxH = max(h, maxH)
        return maxH



import unittest
import collections

null = None
class SolutionTests(unittest.TestCase):
    
    param_list = [
        ([3,9,20,null,null,15,7], 3),
        ([1,null,2], 2),
        ([1], 1),
        ([0], 1),
        ([null], 0),
        ([], 0),
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

    def testCases_maxDepthRec(self):
        for nums, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                root = buildTree(nums)
                # act
                result = s.maxDepthRec(root)
                # assert
                self.assertEqual(expected, result, (nums, root))

    def testCases_maxDepthBFS(self):
        for nums, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                root = buildTree(nums)
                # act
                result = s.maxDepthBFS(root)
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
