from typing import *
import heapq
# 239. Sliding Window Maximum
# https://leetcode.com/problems/sliding-window-maximum/
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = {}
        maxheap, result = [], []

        for i, n in enumerate(nums):
            if not n in window: window[n] = 0
            window[n] += 1
            heapq.heappush(maxheap, -n)

            if i >= k:
                nn = nums[i-k]
                window[nn] -= 1
                if window[nn] == 0: window.pop(nn)
                while -maxheap[0] not in window:
                    heapq.heappop(maxheap)
            if i >= k - 1:
                result.append(-maxheap[0])

        return result


import unittest
null = None
class SolutionTests(unittest.TestCase): 
    param_list = lambda _:[
        ([1,3,-1,-3,5,3,6,7], 3,[3,3,5,5,6,7]),
        ([1,3,1,2,0,5], 3, [3,3,2,5]),
        ([1, -1], 1, [1, -1]),
    ]

    def testCases_maxSlidingWindow(self):
        for nums, k, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.maxSlidingWindow(nums, k)
                # assert
                self.assertEqual(expected, result, (nums, k))

    # def test(self):
    #     self.assertEqual(2, -1)

if __name__ == '__main__':
    unittest.main()
