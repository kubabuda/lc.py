from typing import *
# 2610. Convert an Array Into a 2D Array With Conditions
# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/

class Solution:
    '''list of sets: N space N time'''
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        sets = []
        for n in nums:
            ts = None
            for s in sets:
                if not n in s:
                    ts = s
                    break
            if ts is None:
                ts = set()
                sets.append(ts)
            ts.add(n)
        return [list(s) for s in sets]        

    '''frequency map: N space N time'''
    def findMatrix_freqMap(self, nums: List[int]) -> List[List[int]]:
        freq = {}
        for n in nums:
            if n not in freq:
                freq[n] = 0
            freq[n] += 1
        cnt = max(freq[n] for n in freq)
        result = [[] for i in range(cnt)]
        for n in freq:
            for i in range(freq[n]):
                result[i].append(n)
        return result


import unittest
null = None
class SolutionTests(unittest.TestCase): 
    param_list = lambda _:[
        ([1,3,4,1,2,3,1], [[1,3,4,2],[1,3],[1]]),
        ([1,2,3,4], [[4,3,2,1]]),
    ]

    def testCases_findMatrix(self):
        for nums, expected in self.param_list():
            with self.subTest():
                # arrange
                sol = Solution()
                # act
                result = sol.findMatrix(nums)
                # assert
                self.assertEqual(
                    sorted((sorted(i) for i in expected)),
                    sorted((sorted(i) for i in result)),
                    (nums))

    def testCases_findMatrix_freqMap(self):
        for nums, expected in self.param_list():
            with self.subTest():
                # arrange
                sol = Solution()
                # act
                result = sol.findMatrix_freqMap(nums)
                # assert
                self.assertEqual(
                    sorted((sorted(i) for i in expected)),
                    sorted((sorted(i) for i in result)),
                    (nums))


if __name__ == '__main__':
    unittest.main()
