from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        mapping = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        res = []
        combo = []
        
        def backtrack(i: int):
            if i == len(digits):
                res.append("".join(combo))
                return
            for ch in mapping[digits[i]]:
                combo.append(ch)
                backtrack(i + 1)
                combo.pop()
        
        backtrack(0)
        return res
