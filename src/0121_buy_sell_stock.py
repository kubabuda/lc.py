from typing import *
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """linear O(n) time, O(1) memory"""
        maxProfit = 0
        profit = 0
        minPrice = prices[0]
        for price in prices:
            minPrice = min(minPrice, price)
            profit = price - minPrice
            maxProfit = max(profit, maxProfit)

        return maxProfit

    def maxProfitBruteforce(self, prices: List[int]) -> int:
        """bruteforce: O(n**2) time, O(1) memory"""
        maxProfit = 0
        for bi, buy in enumerate(prices):
            for si, sell in enumerate(prices[bi:]):
                diff = sell - buy
                maxProfit = max(diff, maxProfit)

        return maxProfit
        
from unittest import TestCase
import unittest

class Test(unittest.TestCase): 

    def testCases(self):
        param_list = [
            ([7,1,5,3,6,4], 5),
            ([7,6,4,3,1], 0),
        ]
        for prices, expected in param_list:
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.maxProfit(prices)
                # assert
                self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
