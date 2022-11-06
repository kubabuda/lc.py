from typing import *
import heapq
# 347. Top K Frequent Elements
# https://leetcode.com/top-k-frequent-elements//

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        "Hashmap + sort: O(n) space, O(n log n) time"
        cnt = [(ct, val) for val, ct in Counter(nums).items()]
        return [val for ct, val in sorted(cnt)[::-1][:k]]

    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        "Minheap: O(n) space, O(n log n) time - equivalent to hashmap solution"
        cnt = [(ct, val) for val, ct in Counter(nums).items()]
        klargest = heapq.nlargest(k, cnt)
        return [val for ct, val in klargest]

    def topKFrequentB(self, nums: List[int], k: int) -> List[int]:
        "bucket sort: O(n) space, O(n) time"
        cnt, result = Counter(nums), set()
        freq = [set() for i in range(len(nums) + 1)]

        for n in cnt:
            freq[cnt[n]].add(n)

        for ns in freq[::-1]:
            for n in ns:
                if len(result) >= k: return list(result)
                result.add(n)
        return list(result) # if len(nums) == k

import unittest

class SolutionTests(unittest.TestCase):     
    param_list = lambda _:[
        ([1,1,1,2,2,3], 2, [1,2]),
        ([1], 1, [1]),
    ]

    def testCases_topKFrequent(self):
        for nums, k, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.topKFrequent(nums, k)
                # assert
                self.assertEqual(sorted(expected), sorted(result), (nums))

    def testCases_topKFrequent2(self):
        for nums, k, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.topKFrequent2(nums, k)
                # assert
                self.assertEqual(sorted(expected), sorted(result), (nums))


    def testCases_topKFrequentB(self):
        for nums, k, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.topKFrequentB(nums, k)
                # assert
                self.assertEqual(sorted(expected), sorted(result), (nums))

if __name__ == '__main__':
    unittest.main()
