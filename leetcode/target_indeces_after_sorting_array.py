class Solution(object):
    def targetIndices(self, nums, target):
        res = []
        nums.sort()
        for i,elem in enumerate(nums):
            if elem == target:
                res.append(i)
        return res