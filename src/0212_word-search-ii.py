from os import remove
from typing import *
# 212. Word Search II
# https://leetcode.com/problems/design-add-and-search-words-data-structure/

class Solution:
    def findWords1(self, board: List[List[str]], words: List[str]) -> List[str]:
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


    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = {}
        EOL = '\0'
        
        def addWord(word) -> None:
            node = root
            for c in word:
                if not c in node: node[c] = {}
                node = node[c]
            if not EOL in node: node[EOL] = 0
            node[EOL] += 1

        def pruneWord(word) -> None:
            node = root
            nodes, chars, N = [], [], len(word)
            for c in word:
                nodes.append(node)
                chars.append(c)
                node = node[c]
            node[EOL] -= 1
            if not node[EOL]:
                node.pop(EOL)         
            for i in range(N):
                node, c = nodes[N-i-1], chars[N-i-1]
                if not node[c]:
                    node.pop(c)

        for word in set(words): addWord(word)
        result, visited = set(), set()
        ROWS, COLS = len(board), len(board[0])
        
        def dfs(x, y, node, word=''):
            if x < 0 or x >= ROWS or y < 0 or y >= COLS\
            or (x,y) in visited or not board[x][y] in node: return
            visited.add((x,y))

            c = board[x][y]
            node = node[c]
            word = f'{word}{c}'

            if EOL in node:
                result.add(word)
                pruneWord(word)

            dfs(x-1, y, node, word)
            dfs(x+1, y, node, word)
            dfs(x, y-1, node, word)
            dfs(x, y+1, node, word)
    
            visited.remove((x,y))

        for x in range(ROWS):
            for y in range(COLS):
                dfs(x,y, root)
        
        return list(result)


import unittest
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

    def testCases_findWords(self):
        for board, words, expected in self.param_list:
            with self.subTest():
                # arrange
                sut = Solution()
                # act
                result = sut.findWords(board, words)
                # assert
                self.assertEqual(sorted(expected), sorted(result), (board, words))

    def testCases_findWords1(self):
        for board, words, expected in self.param_list:
            with self.subTest():
                # arrange
                sut = Solution()
                # act
                result = sut.findWords1(board, words)
                # assert
                self.assertEqual(sorted(expected), sorted(result), (board, words))

if __name__ == '__main__':
    unittest.main()
