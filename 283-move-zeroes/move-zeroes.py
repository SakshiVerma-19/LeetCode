class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        left=0
        for i in range(n):
            if (nums[i]!=0):
                nums[left],nums[i]=nums[i], nums[left]
                left+=1
        return nums
        