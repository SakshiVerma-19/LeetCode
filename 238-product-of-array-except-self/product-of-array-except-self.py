from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n =len(nums)
        ans = [1]*n
        # prefix=[1]*n
        # suffix=[1]*n

        prefix=1
        for i in range(1, n):
            ans[i]=ans[i-1]*nums[i-1]
            suffix=1
        for j in range(n-1,-1,-1):
            ans[j]*=suffix
            suffix*=nums[j]
        # for i in range(n):
        #     ans[i]=prefix[i]*suffix[i]
        return ans
