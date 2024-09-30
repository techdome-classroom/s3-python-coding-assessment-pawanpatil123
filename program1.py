class Solution(object):
    def isValid(self, s):
        
        pass


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for char in s:
            # If the character is a closing bracket
            if char in mapping:
                # Pop the topmost element from the stack if it exists, else assign a dummy value
                top_element = stack.pop() if stack else '#'
                
                # The mapping for the closing bracket doesn't match the top element of the stack
                if mapping[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push onto the stack
                stack.append(char)
        
        # If the stack is empty, all the brackets are matched
        return not stack




    



  

