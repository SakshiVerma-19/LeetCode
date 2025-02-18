class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        num = []
        stack = []
        
        for i in range(n + 1):
            stack.append(str(i + 1))
            
            if i == n or pattern[i] == 'I':
                while stack:
                    num.append(stack.pop())
        
        return ''.join(num)
        