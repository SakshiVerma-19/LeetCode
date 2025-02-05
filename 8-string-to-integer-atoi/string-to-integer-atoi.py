class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        s = s.lstrip()
        if not s:
            return 0

        sign = 1
        start = 0
        if s[0] in ('-', '+'):
            if s[0] == '-':
                sign = -1
            start = 1

        result = 0
        for i in range(start, len(s)):
            if not s[i].isdigit():
                break
            result = result * 10 + int(s[i])

        result *= sign

        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        
        return result
