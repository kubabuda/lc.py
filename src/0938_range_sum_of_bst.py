from typing import *
import collections
# 938. Range Sum of BST
# https://leetcode.com/problems/range-sum-of-bst/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return f"TreeNode {self.val}{f' l:({self.left})' if self.left else ''}{f' r:({self.right})' if self.right else ''}"

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = 0
        if root:
            result += self.rangeSumBST(root.left, low, high)
            if low <= root.val <= high: 
                result += root.val
            result += self.rangeSumBST(root.right, low, high)
        return result 


import unittest
import collections

null = None
class SolutionTests(unittest.TestCase):
    
    param_list = [
        ([10,5,15,3,7,null,18], 7, 15, 32),
    ]

    def testCases_rangeSumBST(self):
        for nums, low, high, expected in self.param_list:
            with self.subTest():
                # arrange
                sol = Solution()
                root = buildTree(nums)
                # act
                result = sol.rangeSumBST(root, low, high)
                # assert
                self.assertEqual(expected, result, (root, low, high))


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
