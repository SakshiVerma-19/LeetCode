
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_array=[]
        i, j = 0,0
        while i < len(nums1) and j < len(nums2):
            if nums1[i]<nums2[j]:
                merged_array.append(nums1[i])
                i+=1
            else:
                merged_array.append(nums2[j])
                j+=1
        while i<len(nums1):
            merged_array.append(nums1[i])
            i+=1
        while j<len(nums2):
            merged_array.append(nums2[j])
            j+=1
        n = len(merged_array)
        mid = n//2
        if n%2==0:
            median = (merged_array[mid-1]+merged_array[mid])/2
        else:
            median = merged_array[mid]
        return median

        