class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char == ')':
                # Pop characters until matching '(' is found
                substring = []
                while stack and stack[-1] != '(':
                    substring.append(stack.pop())
                
                # Pop the '('
                stack.pop()
                
                # Push reversed substring back onto the stack
                stack.extend(substring)
            else:
                stack.append(char)
                
        return "".join(stack)