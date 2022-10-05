from typing import *
# 76. Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_s = Counter(s)
        count_t = Counter(t)

        def isWindow():
            for ct in count_t:
                if ct not in count_s or count_s[ct] < count_t[ct]:
                    return False
            return True
        
        if not isWindow(): return ""

        count_s = { c: 0 for c in count_s }
        minL = s
        l = 0    

        for r in range(len(s)):
            count_s[s[r]] += 1
            while isWindow():
                subs = s[l:r+1]
                if len(subs) < len(minL): minL = subs
                count_s[s[l]] -= 1
                l += 1

        return minL


from unittest import TestCase
import unittest

class SolutionTests(unittest.TestCase): 
    
    param_list = lambda self: [
        ("ADOBECODEBANC", "ABC", "BANC"),
        ("a", "a", "a"),
        ("a", "aa", ""),
        ("a", "b", ""),
    ]

    def testCases_minWindow(self):
        for s, t, expected in self.param_list():
            with self.subTest():
                # arrange
                sol = Solution()
                # act
                result = sol.minWindow(s, t)
                # assert
                self.assertEqual(expected, result, (s, t))

if __name__ == '__main__':
    unittest.main()
