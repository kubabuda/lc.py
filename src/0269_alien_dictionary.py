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

        def dfs_populate_preceeding(words, prefix)->bool:
            if not words: return
            prefix_len = len(prefix)
            c_words = {}
            prev_word = ''

            for c_word in words:
                if len(c_word) < len(prev_word) and c_word in prev_word:
                    return False    # invalid input data
                if len(c_word) > prefix_len:
                    c = c_word[prefix_len]
                    if c not in c_words:
                        c_words[c] = []
                    for i in c_words:
                        if i != c:
                            preceeding[c].add(i)
                    if len(c_word) > prefix_len:
                        c_words[c].append(c_word)
                prev_word = c_word

            for c in c_words:
                ch_words = c_words[c]
                if words:
                    c_prefix = f'{prefix}{c}'
                    if not dfs_populate_preceeding(ch_words, c_prefix): return False
            return True
            
        if not dfs_populate_preceeding(words, ''): return ''
        
        result = []
        visited = {}

        def dfs_topo_sort(c)-> bool:
            if c in visited: 
                return visited[c]
            visited[c] = False
            for cc in preceeding[c]:
                if not dfs_topo_sort(cc): return False
            
            result.append(c)
            visited[c] = True

            return True

        for c in letters:
            if not dfs_topo_sort(c): return ''

        return "".join(result)

        
from unittest import TestCase
import unittest
class TestTemplate(unittest.TestCase): 
    
    param_list = [
        (['wrt','wrf','er','ett','rftt'], 'wertf'),
        (['wrt','wrf','er','ett','rftt','rft'], ''), # wrong input sorting
        (['wrt','wrf','er','ett','er','rftt'], ''), # cycles in input graph
    ]

    def testCases(self):
        for words, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.alienOrder(words)
                # assert
                self.assertEqual(expected, result, (words))

if __name__ == '__main__':
    unittest.main()
