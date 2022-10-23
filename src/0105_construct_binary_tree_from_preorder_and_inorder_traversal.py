from typing import *
import collections
# 105. Construct Binary Tree from Preorder and Inorder Traversal
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return f"TreeNode {self.val}{f' l:({self.left})' if self.left else ''}{f' r:({self.right})' if self.right else ''}"

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder: return None
        i = inorder.index(preorder[0])
        root = TreeNode(preorder[0])
        if i:
            root.left = self.buildTree(preorder[1:i+1], inorder[:i])
        if i < len(preorder) - 1:
            root.right = self.buildTree(preorder[i+1:], inorder[i+1:])

        return root


from unittest import TestCase
import unittest
import collections

null = None
class SolutionTests(unittest.TestCase):
    
    param_list = [
        ([3,9,20,15,7], [9,3,15,20,7], [3,9,20,null,null,15,7]),
        ([-1], [-1], [-1]),
    ]

    def testCases_buildTree(self):
        def dfs_assertEqual(n1, n2):
            if (n1 and not n2) or (not n1 and n2):
                self.assertEqual(n1, n2, (n1, n2))
            if n1 and n2:
                self.assertEqual(n1.val, n2.val, (n1, n2))
                if n1.left: dfs_assertEqual(n1.left, n2.left)
                if n1.right: dfs_assertEqual(n1.right, n2.right)

        for preorder, inorder, expected in self.param_list:
            with self.subTest():
                # arrange
                sol = Solution()
                # act
                result = sol.buildTree(preorder, inorder)
                # assert
                expectedTree = buildTree(expected)
                dfs_assertEqual(expectedTree, result)

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
