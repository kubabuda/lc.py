from typing import *
# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if not digits: return result

        button_letters = {         '2':['a','b','c'], '3':['d','e','f'],
            '4':['g','h','i'],     '5':['j','k','l'], '6':['m','n','o'],
            '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']
        }
        rem = self.letterCombinations(digits[1:])
        if rem: 
            for c in button_letters[digits[0]]:
                for r in rem:
                    result.append(f'{c}{r}')
        else:
            result.extend(button_letters[digits[0]])
        
        return result


import unittest
null = None
class SolutionTests(unittest.TestCase): 
    param_list = lambda _:[
        ("23", ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
        ("", []),
        ("2", ["a","b","c"]),
    ]

    def testCases_letterCombinations(self):
        for digits, expected in self.param_list():
            with self.subTest():
                # arrange
                s = Solution()
                # act
                result = s.letterCombinations(digits)
                # assert
                self.assertEqual(set(expected), set(result), (digits))

if __name__ == '__main__':
    unittest.main()
