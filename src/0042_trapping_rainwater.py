from typing import *
# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water

class Solution:
    """Two pointers: O(n) time, O(1) space"""
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, 0
        result = 0

        while right >= left:
            if leftMax < rightMax:
                result += max(0, leftMax - height[left])
                leftMax = max(leftMax, height[left])
                left += 1
            else:
                result += max(0, rightMax - height[right])
                rightMax = max(rightMax, height[right])
                right -= 1
        return result

    """Two lists: O(n) time, O(n) space"""
    def trap_twoLists(self, height: List[int]) -> int:
        left = [0 for i in range(len(height))]
        left[0] = height[0]
        for i in range(1, len(height)):
            left[i] = max(height[i], left[i-1])
        
        right = [0 for i in left]
        right[-1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            right[i] = max(height[i], right[i+1])
        
        result = 0
        for i in range(len(height)):
            result += max(0, min(right[i], left[i])- height[i])

        return result


    """Stack + two pointers. O(n log n) time, O(n) space"""
    def trap_sort(self, height: List[int]) -> int:
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
        ([4,2,3], 1),
        ([3,2,4], 1),
        ([3,0,2], 2),
        ([1,0,1], 1),
        ([0,7,1,4,6], 7),
        ([1,0,0,1], 2),
        ([0,1,0,2,1,0,1,3,2,1,2,1], 6),
        ([4,2,0,3,2,5], 9),
        ([4,9,4,5,3,2], 1)
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

    def testCases_trap_twoLists(self):
        for word, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.trap_twoLists(word)
                # assert
                self.assertEqual(expected, result, (word))

    def testCases_trap_sort(self):
        for word, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.trap_sort(word)
                # assert
                self.assertEqual(expected, result, (word))

if __name__ == '__main__':
    unittest.main()
