class Solution:
    def clearDigits(self, s: str) -> str:
        
        stack = []
        for ch in s:
            if ch.isdigit():
                while stack and stack[-1].isdigit():
                    temp = stack.pop()
                if stack:
                    stack.pop()  
            else:
                stack.append(ch)
        return ''.join(stack)
