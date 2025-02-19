from typing import List
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def backtrack(curr_str: str):
            if len(curr_str)==n:
                result.append(curr_str)
                return
            for char in 'abc':
                if not curr_str or curr_str[-1]!=char:
                    backtrack(curr_str+char)
        result=[]
        backtrack("")
        if k> len(result):
            return ""
        else:
            return result[k-1]
        