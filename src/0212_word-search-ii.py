from os import remove
from typing import *
import collections
# 212. Word Search II
# https://leetcode.com/problems/design-add-and-search-words-data-structure/
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return f"TreeNode {self.val}{f' l:({self.left})' if self.left else ''}{f' r:({self.right})' if self.right else ''}"

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        letters = {}
        for i in range(len(board)):
            for j in range(len(board[0])):
                c = board[i][j]
                if c not in letters: letters[c] = set()
                letters[c].add((i,j))

        def isinboard(word, path=None, prev_xy=None) -> bool:
            if not word: return True
            if word[0] not in letters: return False

            if not path:
                for xy in letters[word[0]]:
                    if isinboard(word[1:], set([xy]), xy): 
                        return True
            else:
                x, y = prev_xy
                curr = [(x - 1, y), (x + 1, y),(x, y - 1), (x, y + 1)]
                for xy in curr:
                    if xy in letters[word[0]] and xy not in path:
                        path.add(xy)
                        if isinboard(word[1:], path, xy):
                            return True
                        path.remove(xy)
            return False

        return [w for w in words if isinboard(w)] 



import unittest
import collections

null, true, false = None, True, False

class SolutionTests(unittest.TestCase):
    
    param_list = [
        (
            [["a","b"],
             ["c","d"]], 
             ["abcb"], []
        ),
        (
            [["o","a","a","n"],
             ["e","t","a","e"],
             ["i","h","k","r"],
             ["i","f","l","v"]],
            ["oath","pea","eat","rain"],
            ["eat","oath"]
        ),
    ]

    def testCases_rangeSumBST(self):
        for board, words, expected in self.param_list:
            with self.subTest():
                # arrange
                sut = Solution()
                # act
                result = sut.findWords(board, words)
                # assert
                self.assertEqual(sorted(expected), sorted(result), (board, words))


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
