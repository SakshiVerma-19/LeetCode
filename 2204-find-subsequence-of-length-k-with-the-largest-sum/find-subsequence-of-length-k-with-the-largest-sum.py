class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        indexed =[(num,i) for i, num in enumerate(nums)]

        top_k =sorted(indexed, key =lambda x: x[0], reverse = True) [:k]
        top_k_sorted = sorted(top_k, key= lambda x:x[1])

        return [num for num, _ in top_k_sorted]
        