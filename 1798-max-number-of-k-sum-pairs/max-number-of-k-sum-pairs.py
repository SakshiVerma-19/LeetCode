class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        from collections import Counter

        count = Counter(nums)
        operations = 0

        for num in nums:
            complement = k - num
            if count[num] > 0 and count[complement] > 0:
                if num == complement:
                    if count[num] >= 2:
                        operations += 1
                        count[num] -= 2
                else:
                    operations += 1
                    count[num] -= 1
                    count[complement] -= 1

        return operations

            