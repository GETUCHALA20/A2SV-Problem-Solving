class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = []
        nums.sort()
        length = len(nums)
        for i in range(length//2):
            res.append(nums[length-1-i])
            res.append(nums[i])
        if length % 2 != 0:
            res.append(nums[length//2])
        return res