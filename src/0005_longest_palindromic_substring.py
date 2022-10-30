from typing import *
# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        "O(n**2) time O(1) space"
        N = len(s)
        maxL, maxR, maxLen = 0, 0, 0
        for i in range(N):
            l = r = i
            while l >= 0 and r < N and s[l] == s[r]:
                if r - l > maxLen:
                    maxL, maxR = l, r
                    maxLen = r - l
                l -= 1
                r += 1
            l = i
            r = l + 1
            while l >= 0 and r < N and s[l] == s[r]:
                if r - l > maxLen:
                    maxL, maxR = l, r
                    maxLen = r - l
                l -= 1
                r += 1
        return s[maxL:maxR+1]

    def longestPalindromeManacher(self, s: str) -> str:
        "O(n) time O(n) space"
        N = len(s)
        if N < 2: return s
        st = f'${s}^'

        Re = [0 for i in range(N + 2)] # even palindrome
        i = t = 0
        while i <= N: 
            while st[i - t] == st[i + t + 1]: t += 1
            Re[i] = t
            k = 1
            
            while k <= t and Re[i - k] != Re[i] - k:
                Re[i + k] = min(Re[i - k], Re[i] - k)
                k += 1
            t -= k
            t = max(0,t)
            i += k
        
        Ro = [0 for i in range(N + 2)] # odd palindrome
        i = t = 0
        while i <= N: 
            while st[i - t - 1] == st[i + t + 1]: t += 1
            Ro[i] = t
            k = 1
            
            while k <= t and Ro[i - k] != Ro[i] - k:
                Ro[i + k] = min(Ro[i - k], Ro[i] - k)
                k += 1
            t -= k
            t = max(0,t)
            i += k
        
        maxRo, io = max((l, i) for i,l in enumerate(Ro))
        maxRe, ie = max((l, i) for i,l in enumerate(Re))
        if maxRo >= maxRe:
            if not maxRo: return st[1]
            return st[io - maxRo : io + maxRo + 1]
        else:
            return st[ie - maxRe + 1 : ie + maxRe + 1]



import unittest

class SolutionTests(unittest.TestCase): 
    
    param_list = lambda self: [
        ("abba", "abba"),
        ("aba", "aba"),
        ("abb", "bb"),
        ("abc", "a"),
        ("cbbd", "bb"),
        ("b", "b"),
    ]

    def testCases_longestPalindrome(self):
        for s, expected in self.param_list():
            with self.subTest():
                # arrange
                sol = Solution()
                # act
                result = sol.longestPalindrome(s)
                # assert
                self.assertEqual(len(result), len(expected), f'{s}: {result} != {expected}')
                self.assertTrue(result in s, f'{s}: {result} not in {expected}')

    def testCases_longestPalindromeManacher(self):
        for s, expected in self.param_list():
            with self.subTest():
                # arrange
                sol = Solution()
                # act
                result = sol.longestPalindromeManacher(s)
                # assert
                self.assertEqual(len(result), len(expected), f'{s}: {result} != {expected}')
                self.assertTrue(result in s, f'{s}: {result} not in {s}')

if __name__ == '__main__':
    unittest.main()
