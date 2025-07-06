class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.count2 = Counter(nums2)
        

    def add(self, index: int, val: int) -> None:
        old_val =  self.nums2[index]
        self.count2[old_val] -= 1
        if self.count2[old_val] == 0:
            del self.count2[old_val]
        self.nums2[index]+=val
        new_val = self.nums2[index]
        self.count2[new_val] += 1
        

    def count(self, tot: int) -> int:
        result = 0
        for a in self.nums1:
            b = tot - a
            result += self.count2.get(b,0)
        return result
        


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)