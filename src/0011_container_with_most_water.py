from typing import *
# https://leetcode.com/problems/container-with-most-water
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        area = 0
        start = 0
        end = len(height) - 1
        while start < end:
            area = min(height[start], height[end]) * (end - start)
            maxArea = max(area, maxArea)
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
        return maxArea
    
    def maxArea2(self, height: List[int]) -> int:
        maxArea = 0
        openedC = []    # opened containers, in order
        openedC_start = {} # height: index
        for i, h in enumerate(height):
            anyC = False
            for ah in openedC_start:
                if ah > h:
                    if anyC:
                        break
                    anyC = True
                area = min(ah, h) * (i - openedC_start[ah])
                maxArea = max(area, maxArea)
            if not openedC or h > openedC[-1]:
                openedC.append(h)
                openedC_start[h] = i
        return maxArea

    def maxAreaBruteforce(self, height: List[int]) -> int:
        maxArea = 0
        for i1, n1 in enumerate(height[:-1]):
            for i2, n2 in enumerate(height[(i1+1):]):
                h = min(n1, n2)
                l = i2 + 1
                area = h * l
                maxArea = max(area, maxArea)
        return maxArea

from unittest import TestCase
import unittest

class SolutionTests(unittest.TestCase): 
    def testCases(self):
        param_list = [
            ([1,8,6,2,5,4,8,3,7], 49),
            ([1,1], 1),
        ]
        for nums, expected in param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.maxArea(nums)
                # assert
                self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
