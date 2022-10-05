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
        minL = (0, len(s))
        l = 0    

        for r in range(len(s)):
            count_s[s[r]] += 1
                
            while isWindow():
                if (r+1-l) < minL[1]-minL[0]:
                    minL = (l, r+1)
                count_s[s[l]] -= 1
                l += 1

        return s[minL[0]:minL[1]]


    def minWindowF(self, s: str, t: str) -> str:
        count_t = Counter(t)
        filtr_s = [(i, c) for i,c in enumerate(s) if c in count_t]
        count_s = Counter(c for i,c in filtr_s)

        def isWindow():
            for ct in count_t:
                if ct not in count_s or count_s[ct] < count_t[ct]:
                    return False
            return True
        
        if not isWindow(): return ""

        count_s = { c: 0 for c in count_t }
        minL = (0, len(s))
        filtr_l = 0

        for r, c in filtr_s:
            count_s[c] += 1

            while isWindow():
                l, cl = filtr_s[filtr_l]
                if (r+1-l) < minL[1]-minL[0]:
                    minL = (l, r+1)
                count_s[cl] -= 1
                filtr_l += 1

        return s[minL[0]:minL[1]]


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

    def testCases_minWindowF(self):
        for s, t, expected in self.param_list():
            with self.subTest():
                # arrange
                sol = Solution()
                # act
                result = sol.minWindowF(s, t)
                # assert
                self.assertEqual(expected, result, (s, t))

if __name__ == '__main__':
    unittest.main()
