from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # stack holds the current parenthesis sequence being built
        stack = []
        res = []

        def backtrack(openN, closedN):
            # Base Case: We've used all n open and n closed parentheses.
            if openN == n and closedN == n:
                res.append("".join(stack))
                return

            # 1. Option to add an Open Parenthesis '('
            # We can only add an open parenthesis if we haven't used all n of them.
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop() # Backtrack: remove the '(' for the next path

            # 2. Option to add a Closed Parenthesis ')'
            # We can only add a closed parenthesis if there are more open ones
            # currently in the string to close. This is the validity check.
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop() # Backtrack: remove the ')' for the next path

        # Start the process with 0 open and 0 closed parentheses
        backtrack(0, 0)
        return res

# Example Usage:
# sol = Solution()
# print(sol.generateParenthesis(3)) 
# Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]
