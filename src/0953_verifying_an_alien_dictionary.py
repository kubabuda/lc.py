from typing import *
# from collections import deque
# https://leetcode.com/problems/alien-dictionary
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        c_order = { c:i for i,c in enumerate(order) } # a:0, b:1

        def is_sorted_dfs(start, end, offset) -> bool:
            while start < len(words) and len(words[start]) < offset: start += 1
            while end > 0 and len(words[end]) < offset: end -= 1
            if start >= end: return True
            ranges = set()
            curr_start = start
            prev_word = words[start]
            

            for i in range(start + 1, end + 1):
                curr_word = words[i]
                if len(prev_word) > offset and len(curr_word) > offset:
                    curr_c = curr_word[offset]
                    prev_c = prev_word[offset]
                    if curr_c != prev_c:
                        if c_order[curr_c] < c_order[prev_c]:
                            return False
                        else:
                            ranges.add((curr_start, i-1))
                            curr_start = i
                elif len(prev_word) > offset and len(curr_word) <= offset:
                    return False # longer word should be after shorter one
                prev_word = curr_word
            ranges.add((curr_start, end))

            for c_start, c_end in ranges:
                if not is_sorted_dfs(c_start, c_end, offset + 1): return False
            return True

        return is_sorted_dfs(0, len(words) - 1, 0)
        
        
from unittest import TestCase
import unittest
class TestTemplate(unittest.TestCase): 
    
    param_list = [
        (["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz", True),
        (["word","world","row"], "worldabcefghijkmnpqstuvxyz", False),
        (["apple","app"], "abcdefghijklmnopqrstuvwxyz", False),
        (["hello","hello"], "abcdefghijklmnopqrstuvwxyz", True),
    ]

    def testCases(self):
        for words, order, expected in self.param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.isAlienSorted(words, order)
                # assert
                self.assertEqual(expected, result, (words))

if __name__ == '__main__':
    unittest.main()
