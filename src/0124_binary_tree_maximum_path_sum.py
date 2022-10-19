from typing import *
import collections
import heapq
# 124. Binary Tree Maximum Path Sum
# https://leetcode.com/problems/binary-tree-maximum-path-sum/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return f"TreeNode {self.val}{f' l:({self.left})' if self.left else ''}{f' r:({self.right})' if self.right else ''}"

class Solution:

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        minheap = []

        def maxSubpathSum(root) -> int:
            """O(n) space"""
            possible = [-root.val] # flip sign to use minheap

            if root.left:
                l = maxSubpathSum(root.left)
                possible.append(l - root.val)
            if root.right: 
                r = maxSubpathSum(root.right)
                possible.append(r - root.val)
            p = min(possible)
            heapq.heappush(minheap, p)
            
            if root.left and root.right:
                detechedVal = r + l - root.val
                if detechedVal < p:
                    heapq.heappush(minheap, detechedVal)
            
            return p
    
        maxSubpathSum(root)

        return 0 - minheap[0] # flip sign back

    def maxPathSum1(self, root: Optional[TreeNode]) -> int:
        """O(1) space"""
        maxSum = root.val

        def maxSubpathSum(root) -> int:
            possible = [root.val]
            nonlocal maxSum

            if root.left:
                l = maxSubpathSum(root.left)
                possible.append(l + root.val)
            if root.right: 
                r = maxSubpathSum(root.right)
                possible.append(r + root.val)
            p = max(possible)
            maxSum = max(p, maxSum)
            
            if root.left and root.right:
                detechedVal = r + l + root.val
                if detechedVal > p:
                    maxSum = max(detechedVal, maxSum)
            
            return p
    
        maxSubpathSum(root)
        return maxSum



from unittest import TestCase
import unittest
import collections

null = None
class SolutionTests(unittest.TestCase):
    
    param_list = [
        ([1,2,3], 6),
        ([-10,9,20,null,null,15,7], 42),
        ([1,-2,-3,1,3,-2,null,-1], 3),
        ([5,4,8,11,null,13,4,7,2,null,null,null,1], 48),
    ]

    def testCases_maxPathSum(self):
        for nums, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                root = buildTree(nums)
                # act
                result = s.maxPathSum(root)
                # assert
                self.assertEqual(expected, result, (nums, root))

    def testCases_maxPathSum1(self):
        for nums, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                root = buildTree(nums)
                # act
                result = s.maxPathSum1(root)
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
