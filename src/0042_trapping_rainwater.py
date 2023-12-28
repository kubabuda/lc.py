from typing import *
# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water

class Solution:
    """Stack + two pointers. O(n log n) time, O(n) space"""
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        peaks = [(i, h) for i, h in enumerate(height) if 
            i > 0 and i < len(height) - 1 
            and height[i - 1] <= height[i] >= height[i+1]
        ]
        if height[0] > height[1]:
            peaks.append((0, height[0]))
        if height[-1] > height[-2]:
            peaks.append((len(height) - 1, height[-1]))
        peaks.sort(key=lambda h: h[1])
        
        trappedWater = 0
        l = r = peaks.pop()[0]
        while peaks:
            i, h = peaks.pop()
            while i < l:
                trappedWater += max(h - height[l], 0)
                l -= 1
            while i > r:
                trappedWater += max(h - height[r], 0)
                r += 1

        return trappedWater


import unittest

class SolutionTests(unittest.TestCase): 
    
    param_list = lambda _: [
        # ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
        ([4,2,0,3,2,5], 9),
    ]

    def testCases_trap(self):
        for word, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.trap(word)
                # assert
                self.assertEqual(expected, result, (word))

if __name__ == '__main__':
    unittest.main()
