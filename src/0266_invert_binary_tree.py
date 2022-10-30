from typing import *
import collections
# 266. Invert Binary Tree
# https://leetcode.com/problems/invert-binary-tree/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return f"TreeNode {self.val}{f' l:({self.left})' if self.left else ''}{f' r:({self.right})' if self.right else ''}"

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = root.right, root.left
            if root.left: self.invertTree(root.left)
            if root.right: self.invertTree(root.right)
        return root



import unittest
import collections

null = None
class SolutionTests(unittest.TestCase):
    
    param_list = [
        ([4,2,7,1,3,6,9], [4,7,2,9,6,3,1]),
    ]

    def testCases_invertTree(self):
        for nums, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                root = buildTree(nums)
                # act
                result = s.invertTree(root)
                # assert
                resultnums = treeToListBFS(result)
                self.assertEqual(expected, resultnums, (nums, root))


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


def treeToListBFS(root: Optional[TreeNode]) -> List[int]:
    result = []
    if not root: return result
    toVisit = queue = collections.deque([root])
    while toVisit:
        n = toVisit.popleft()
        result.append(n.val)
        if n.left: toVisit.append(n.left)
        if n.right: toVisit.append(n.right)
    
    return result

if __name__ == '__main__':
    unittest.main()
