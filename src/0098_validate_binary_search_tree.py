from typing import *
import collections
# 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return f"TreeNode {self.val}{f' l:({self.left})' if self.left else ''}{f' r:({self.right})' if self.right else ''}"

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isValid_dfs(root):
            valid = True
            minval, maxval = root.val, root.val
            if root.left:
                valid, minl, maxl = isValid_dfs(root.left)
                if root.val <= maxl:
                    return False, False, False
                minval = min(minl, minval)
                maxval = max(maxl, maxval)
            if valid and root.right:
                valid, minr, maxr = isValid_dfs(root.right)
                if root.val >= minr:
                    return False, False, False
                minval = min(minr, minval)
                maxval = max(maxr, maxval)
            return valid, minval, maxval
        
        result, _, _ = isValid_dfs(root)

        return result              


from unittest import TestCase
import unittest
import collections

null = None
class SolutionTests(unittest.TestCase):
    
    param_list = [
        ([1], True),
        ([2,1,3], True),
        ([2,4,3], False),
    ]

    def testCases_isValidBST(self):
        for preorder, expected in self.param_list:
            with self.subTest():
                # arrange
                sol = Solution()
                root = buildTree(preorder)
                # act
                result = sol.isValidBST(root)
                # assert
                self.assertEqual(expected, result, (root))


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
