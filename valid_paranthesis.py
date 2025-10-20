class Solution:
    def isValid(self, s: str) -> bool:
        # Create a stack to store opening brackets
        stack = []
        
        # Dictionary to map closing brackets to their corresponding opening brackets
        closeToOpen = {
            ")": "(", 
            "]": "[", 
            "}": "{"
        }
        
        for char in s:
            if char in closeToOpen:
                # This is a closing bracket
                
                # 1. Check if the stack is NOT empty AND 
                # 2. The top of the stack matches the expected opening bracket
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()  # Matched, remove the opening bracket
                else:
                    return False # Mismatch or closing bracket with no opener
            else:
                # This is an opening bracket, push it onto the stack
                stack.append(char)
        
        # The string is valid only if the stack is empty at the end,
        # meaning every opening bracket was correctly closed.
        return not stack

