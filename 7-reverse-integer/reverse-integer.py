class Solution:
    def reverse(self, x: int) -> int:
        INT_MIN = -2**31
        INT_MAX = 2**31-1

        negative = x<0
        x= abs(x)
        rev = 0

        while x!=0:
            temp = x%10
            rev = rev*10 + temp
            x //=10

        if negative:
            rev = -rev 
            
        if rev >INT_MAX or rev <INT_MIN:
            return 0

        return rev