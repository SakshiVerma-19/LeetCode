class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        
        n = len(nums)
        different_binary_string = ''.join('0' if nums[i][i] == '1' else '1' for i in range(n))
        return different_binary_string