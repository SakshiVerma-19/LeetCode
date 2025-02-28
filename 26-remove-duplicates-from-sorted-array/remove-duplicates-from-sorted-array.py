class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums)) 
        n =len(nums)
        for i in range(len(nums)):
            nums.append('_')

        return n


        


        