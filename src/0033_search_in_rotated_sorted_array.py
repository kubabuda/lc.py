from typing import *
# https://leetcode.com/problems/search-in-rotated-sorted-array
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # single pass approach
        begin = 0
        end = len(nums) - 1
        while begin <= end:
            if nums[end] == target:
                return end
            if nums[begin] == target:
                return begin
            mid = int((begin + end) / 2)
            if nums[mid] == target:
                return mid
            if ((nums[begin] < target < nums[mid] < nums[end]) 
            or (nums[mid] < nums[end] < nums[begin] < target)
            or (target < nums[mid] < nums[end] < nums[begin])
            or (nums[end] < nums[begin] < target < nums[mid])): # target in left half
                end = mid - 1
            else:
                begin = mid + 1
        return -1        

    def search2pass(self, nums: List[int], target: int) -> int:
        # two pass approach
        # find pivot point
        begin = 0
        end = len(nums) - 1
        while begin < end:
            mid = int((begin + end) / 2)
            if end - begin >= 2 and nums[mid] < nums[mid + 1] < nums[mid - 1]:
                begin = mid
                break
            elif nums[mid] > nums[end]: # pivot in right half
                begin = mid + 1
            else:   # pivot point in left half
                end = mid - 1
        pivot_k = begin
        # find value
        begin = 0
        end = len(nums) - 1
        while begin <= end:
            mid = int((begin + end) / 2)
            mid_rotated = (mid + pivot_k) % len(nums)
            if nums[mid_rotated] == target:
                return mid_rotated
            elif nums[mid_rotated] > target:
                end = mid - 1
            else:
                begin = mid + 1
        return -1



import unittest

class Test(unittest.TestCase): 
    
    def testCases(self):
        param_list = [
            ([4,5,6,7,0,1,2], 0, 4),
            ([4,5,6,7,0,1,2], 3, -1),
            ([1], 0, -1),
            ([5,1,3], 5, 0)
        ]
        for nums, target, expected in param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.search(nums, target)
                # assert
                self.assertEqual(expected, result, (nums, target))

if __name__ == '__main__':
    unittest.main()
