class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        n = len(candies)
        max_candy = max(candies)
        return[candy+extraCandies>=max_candy for candy in candies]
        