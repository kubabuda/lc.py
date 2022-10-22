from typing import *
import collections
# 572. Subtree of Another Tree
# https://leetcode.com/problems/subtree-of-another-tree/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return f"TreeNode {self.val}{f' l:({self.left})' if self.left else ''}{f' r:({self.right})' if self.right else ''}"

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode], seekRoot=True) -> bool:
        if root == subRoot == None:
            return True
        elif not root or not subRoot:
            return False
        if root.val == subRoot.val:
            if self.isSubtree(root.left, subRoot.left, False) and self.isSubtree(root.right, subRoot.right, False):
                return True

        return seekRoot and (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))


from unittest import TestCase
import unittest
import collections

null = None
class SolutionTests(unittest.TestCase):
    
    param_list = [
        ([1,2,3], [2], True),
        ([], [2], False),
        ([1,1], [1], True),
        ([3,4,5,1,2], [4,1,2], True),
        ([3,4,5,1,2,null,null,null,null,0], [4,1,2], False),
        ([3,4,5,1,null,2], [3,1,2], False)
    ]

    def testCases_isSubtree(self):
        for nums1, nums2, expected in self.param_list:
            with self.subTest():
                # arrange
                root, candidate = buildTree(nums1), buildTree(nums2)
                sol = Solution()
                # act
                result = sol.isSubtree(root, candidate)
                # assert
                self.assertEqual(expected, result, (root, candidate))
    

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
