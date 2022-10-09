from typing import *
# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """O(m*n log n) time"""
        groups = {}
        for s in strs:
            ss = "".join(sorted(s))
            if ss not in groups:
                groups[ss] = []
            groups[ss].append(s)

        return groups.values()

    def groupAnagramsH(self, strs: List[str]) -> List[List[str]]:
        """O(m*n) time"""
        groups = {}
        ord_a = ord('a')
        for s in strs:
            sc = Counter(s)
            ss = 0
            for c in (chr(ord_a + i) for i in range(26)):
                ss |= sc[c]
                ss <<= 14
            if ss not in groups:
                groups[ss] = []
            groups[ss].append(s)

        return groups.values()

from unittest import TestCase
import unittest

class SolutionTests(unittest.TestCase): 
    
    param_list = lambda self: [
        ([], []),
        ([""], [[""]]),
        (["a"], [["a"]]),
        (["eat","tea","tan","ate","nat","bat"], [["bat"],["nat","tan"],["ate","eat","tea"]]),
        (["cab","tin","pew","duh","may","ill","buy","bar","max","doc"], [["max"],["buy"],["doc"],["may"],["ill"],["duh"],["tin"],["bar"],["pew"],["cab"]]),
        (["cat","rye","aye","cud","cat","old","fop","bra"], [["bra"],["old"],["cud"],["aye"],["rye"],["fop"],["cat","cat"]]),
    ]

    def testCases_groupAnagrams(self):
        for strs, expected in self.param_list():
            with self.subTest():
                # arrange
                sol = Solution()
                # act
                result = sol.groupAnagrams(strs)
                # assert
                self.maxDiff = None
                self.assertEqual(
                    [set(gr) for gr in sorted(sorted(s) for s in expected)], 
                    [set(gr) for gr in sorted(sorted(s) for s in result)],
                    (strs))

    def testCases_groupAnagramsH(self):
        for strs, expected in self.param_list():
            with self.subTest():
                # arrange
                sol = Solution()
                # act
                result = sol.groupAnagramsH(strs)
                # assert
                self.maxDiff = None
                self.assertEqual(
                    [set(gr) for gr in sorted(sorted(s) for s in expected)], 
                    [set(gr) for gr in sorted(sorted(s) for s in result)],
                    (strs))

if __name__ == '__main__':
    unittest.main()
