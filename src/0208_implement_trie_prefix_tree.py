from typing import *
import collections
# 208. Implement Trie (Prefix Tree)
# https://leetcode.com/problems/implement-trie-prefix-tree/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return f"TreeNode {self.val}{f' l:({self.left})' if self.left else ''}{f' r:({self.right})' if self.right else ''}"


class Trie:

    def __init__(self):
        self.root = {}
        self.endChar = '\0'

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node[self.endChar] = None

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node: 
                return False
            node = node[c]
        return self.endChar in node

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node: 
                return False
            node = node[c]
        return True


import unittest
import collections

null, true, false = None, True, False

class SolutionTests(unittest.TestCase):
    
    param_list = [
        (["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
         [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]],
         [null, null, true, false, true, null, true]
        ),
    ]

    def testCases_rangeSumBST(self):
        for commands, params, expected in self.param_list:
            with self.subTest():
                # arrange
                sut = Trie()
                
                for i, cmd in enumerate(commands):
                    if cmd == 'Trie':
                        sut = Trie()
                    elif cmd == 'insert':
                        # act
                        sut.insert(params[i][0])
                    elif cmd == 'search':
                        val, exp = params[i][0], expected[i]
                        # act
                        result = sut.search(val)
                        # assert
                        self.assertEqual(exp, result, (cmd, val))
                    elif cmd == 'startsWith':
                        val, exp = params[i][0], expected[i]
                        # act
                        result = sut.startsWith(val)
                        # assert
                        self.assertEqual(exp, result, (cmd, val))
                    else:
                        self.assertEqual("FAIL", cmd, (i))

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
