from typing import *
import collections
# 211. Design Add and Search Words Data Structure
# https://leetcode.com/problems/design-add-and-search-words-data-structure/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return f"TreeNode {self.val}{f' l:({self.left})' if self.left else ''}{f' r:({self.right})' if self.right else ''}"


class WordDictionary:

    EOL = '\0'
    MATCH_ALL = '.'

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node: node[c] = {}
            node = node[c]
        node[self.EOL] = None

    def search(self, word: str) -> bool:
        def search(word: str, node) -> bool:
            if not word: 
                return node and self.EOL in node
            c, wordtail =  word[0], word[1:]
            if c in node:
                return search(wordtail, node[c])
            elif c == self.MATCH_ALL:
                for c in node:
                    if c is not self.EOL:
                        if search(wordtail, node[c]): return True
            return False
        
        return search(word, self.root)


import unittest
import collections

null, true, false = None, True, False

class SolutionTests(unittest.TestCase):
    
    param_list = [
        (
            ["WordDictionary","addWord","addWord","addWord","search","search","search","search"],
            [[],              ["bad"],  ["dad"],  ["mad"],  ["pad"], ["bad"],  [".ad"],["b.."]],
            [null,            null,     null,      null,    false,   true,     true,   true]
        ),
        (
            ["WordDictionary","addWord","addWord","search","search","search","search","search","search"],
            [[],              ["a"],    ["a"],     ["."],   ["a"],  ["aa"], ["a"],    [".a"],   ["a."]],
            [null,            null,     null,      true,    true,   false,  true,     false,    false]
        ),
        (
            ["WordDictionary","addWord","addWord","addWord","addWord","search","search","addWord","search","search","search","search","search","search"],
            [[],              ["at"],   ["and"],  ["an"],   ["add"],  ["a"],   [".at"], ["bat"],  [".at"], ["an."], ["a.d."],["b."],  ["a.d"], ["."]],
            [null,             null,    null,      null,     null,     false,   false,   null,     true,    true,    false,   false,   true,    false]
        ),
    ]

    def testCases_rangeSumBST(self):
        for commands, params, expected in self.param_list:
            with self.subTest():
                # arrange
                sut = WordDictionary()
                
                for i, cmd in enumerate(commands):
                    if cmd == 'WordDictionary':
                        sut = WordDictionary()
                    elif cmd == 'addWord':
                        # act
                        sut.addWord(params[i][0])
                    elif cmd == 'search':
                        val, exp = params[i][0], expected[i]
                        # act
                        result = sut.search(val)
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
