class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n= len(nums) 
        nums.sort()
        count=0
        longest=0
        lastsmaller=float('-inf')
        for i in range(0,n):
            if nums[i]-1==lastsmaller:
                count+=1
                lastsmaller=nums[i]
            elif nums[i]!=lastsmaller:
                count=1
                lastsmaller=nums[i]
            longest=max(longest, count)

        return longest


        