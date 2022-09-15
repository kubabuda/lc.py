from typing import *
# from collections import deque
# https://leetcode.com/problems/alien-dictionary
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        letters = set()
        for w in words: 
            for c in w: letters.add(c)
        # build prerequisites dictionary
        preceeding = { c: set() for c in letters }

        def bfs_populate_preceeding(words, prefix):
            if not words: return
            prefix_len = len(prefix)
            c_words = {}

            for c_word in words:
                if len(c_word) > prefix_len:
                    c = c_word[prefix_len]
                    if c not in c_words:
                        c_words[c] = []
                        for i in c_words:
                            if i != c:
                                preceeding[c].add(i)
                    if len(c_word) > prefix_len:
                        c_words[c].append(c_word)
            for c in c_words:
                ch_words = c_words[c]
                if words:
                    c_prefix = f'{prefix}{c}'
                    bfs_populate_preceeding(ch_words, c_prefix)
            
        bfs_populate_preceeding(words, '')
        
        result = []
        resultSet = set()

        def dfs_topo_sort(c):
            if c in resultSet: 
                return
            for cc in preceeding[c]:
                dfs_topo_sort(cc)
            result.append(c)
            resultSet.add(c)

        for c in letters:
            dfs_topo_sort(c)

        return "".join(result)

        
from unittest import TestCase
import unittest
class TestTemplate(unittest.TestCase): 
    
    param_list = [
        (['wrt','wrf','er','ett','rftt'], 'wertf'),
    ]

    def testCases(self):
        for words, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.alienOrder(words)
                # assert
                self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()