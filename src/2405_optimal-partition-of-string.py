from typing import *

# 2405. Optimal Partition of String
# https://leetcode.com/problems/optimal-partition-of-string

class Solution:
    '''O(N) time'''
    def partitionString(self, s: str) -> int:
        result = 1
        st = set()
        for c in s:
            if c in st:
                result += 1
                st.clear()
            st.add(c)

        return result
        
    

import unittest
null = None
class SolutionTests(unittest.TestCase): 
    param_list = lambda _:[
        ('abacaba', 4),
        ('ssssss', 6),
        ('hdklqkcssgxlvehva', 4)
    ]

    def testCases_partitionString(self):
        for s, expected in self.param_list():
            with self.subTest():
                # arrange
                sol = Solution()
                # act
                result = sol.partitionString(s)
                # assert
                self.assertEqual(expected, result, (s))

if __name__ == '__main__':
    unittest.main()
