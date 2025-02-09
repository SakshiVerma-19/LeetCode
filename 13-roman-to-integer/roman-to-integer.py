class Solution:
    def romanToInt(self, s: str) -> int:
        Roman={ 'I':1,
                'V':5,
                'X':10,
                'L':50,
                'C':100,
                'D':500,
                'M':1000,
        }
        
        prev = 0
        res=0
        for char in reversed(s):
            value = Roman[char]
            if value < prev:
                res -= value
            else:
                res += value
                prev = value
        return res

        