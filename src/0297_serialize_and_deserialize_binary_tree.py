from typing import *
import collections
# 297. Serialize and Deserialize Binary Tree
# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return f"TreeNode {self.val}{f' l:({self.left})' if self.left else ''}{f' r:({self.right})' if self.right else ''}"

class Codec:
    
    def serialize(self, root):
        values = []
        q = collections.deque([root])
        
        while q:
            n = q.popleft()
            if n:
                values.append(n.val)
                q.append(n.left)
                q.append(n.right)
            else:
                values.append("None")
        
        return ";".join(str(i) for i in values)
        

    def deserialize(self, data):
        values = [ int(v) if v != "None" else None for v in data.split(';')]
        # if not values or not values[0] and values[0] != 0: return None
        
        root = None
        q = collections.deque()

        for i, v in enumerate(values):
            curr = None
            if v != None: 
                curr = TreeNode(v)
                q.append(curr)
            if not root:
                root = curr
            else:
                if i & 1:
                    q[0].left = curr
                else:
                    q[0].right = curr
                    q.popleft()

        return root


from unittest import TestCase
import unittest
import collections

null = None
class CodecTests(unittest.TestCase):
    
    param_list = [
        ([1,2,3]),
        ([1,2,3,null,null,4,5]),
        ([]),
        ([4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]),
    ]

    def testCases_levelOrder(self):
        def dfs_assertEqual(n1, n2):
            if (n1 and not n2) or (not n1 and n2):
                self.assertEqual(n1, n2, (n1, n2))
            if n1 and n2:
                self.assertEqual(n1.val, n2.val, (n1, n2))
                if n1.left: dfs_assertEqual(n1.left, n2.left)
                if n1.right: dfs_assertEqual(n1.right, n2.right)

        for nums  in self.param_list:
            with self.subTest():
                # arrange
                root = buildTree(nums)
                # act
                ser = Codec()
                deser = Codec()
                ans = deser.deserialize(ser.serialize(root))
                # assert
                dfs_assertEqual(root, ans)

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
