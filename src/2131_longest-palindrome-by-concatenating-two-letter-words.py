from typing import *
# 2131. Longest Palindrome by Concatenating Two Letter Words
# https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/

class Solution:

    def longestPalindrome(self, words: List[str]) -> int:
        cnt = Counter(words)
        midpt = False
        result = 0
        
        for word, wc in cnt.items():
            rev = word[::-1]
            if word == rev:
                if wc >= 2:
                    result += 4 * (wc // 2)
                if not midpt and wc % 2:
                    midpt = True
                    result += 2
            elif rev in cnt and cnt[rev] > 0:
                result += 4 * min(wc, cnt[rev])
                cnt[rev] = 0
                cnt[word] = 0
        return result

    def longestPalindrome2(self, words: List[str]) -> int:
        cnt = Counter(words)
        midpt = False
        result = 0
        
        for word in words:
            rev = word[::-1]
            if word == rev:
                if cnt[word] >= 2:
                    result += 4
                    cnt[word] -= 2
                elif not midpt and cnt[word] > 0:
                    midpt = True
                    result += 2
                    cnt[word] -= 1
            elif word != rev and rev in cnt:
                if cnt[word] > 0 and cnt[rev] > 0:
                    result += 4
                    cnt[word] -= 1
                    cnt[rev] -= 1
        return result

import unittest

class SolutionTests(unittest.TestCase): 
    
    param_list = lambda _:[
        (["lc","cl","gg"], 6),
        (["cc","ll","xx"], 2),
        (["ab","ty","yt","lc","cl","ab"], 8),
        (["ll","lb","bb","bx","xx","lx","xx","lx","ll","xb","bx","lb","bb","lb","bl","bb","bx","xl","lb","xx"], 26),
        (['bb', 'bb'], 4),
    ]

    def testCases_longestPalindrome(self):
        for nums, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.longestPalindrome(nums)
                # assert
                self.assertEqual(expected, result, (nums))

    def testCases_longestPalindrome2(self):
        for nums, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.longestPalindrome2(nums)
                # assert
                self.assertEqual(expected, result, (nums))

if __name__ == '__main__':
    unittest.main()
