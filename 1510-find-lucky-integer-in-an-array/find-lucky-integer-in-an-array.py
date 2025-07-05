class Solution:
    def findLucky(self, arr: List[int]) -> int:
        n=len(arr)
        freq ={}
        for i in arr:
            if i in freq:
                freq[i] +=1
            else: 
                freq[i]=1
        maxLuck =- 1
        for i in freq:
            if i == freq[i]:
                if i > maxLuck:
                    maxLuck = i

        return maxLuck


        