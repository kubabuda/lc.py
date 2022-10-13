from typing import *
# 271. Encode and Decode Strings
# https://leetcode.com/problems/encode-and-decode-strings

class Solution:
    def encode(self, strs: List[str]) -> str:
        prefix = ";".join(str(len(s)) for s in strs)
        body = "".join(strs)
        return f"{prefix}:{body}"

    def decode(self, s: str) -> List[str]:
        i = s.find(":")
        lengths = [int(l) for l in s[:i].split(';')]
        start = i + 1
        result = []
        for le in lengths:
            result.append(s[start:start+le])
            start += le
        return result

from unittest import TestCase
import unittest

class SolutionTests(unittest.TestCase): 
    
    param_list = lambda self: [
        (["abc", "abd", "x,y,z"], ["abc", "abd", "x,y,z"]),
        ([";:-!\0"], [";:-!\0"]),
    ]

    def testCases_longestPalindrome(self):
        for s, expected in self.param_list():
            with self.subTest():
                # arrange
                sol = Solution()
                # act
                encoded = sol.encode(s)
                result = sol.decode(encoded)
                # assert
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
