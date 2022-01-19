class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        res = []
        sorted_arr = sorted(nums)
        d = {}
        for i,elem in enumerate(sorted_arr):
            if elem not in d:
                d[elem] = i
        for elem in nums:
            res.append(d[elem])
        return res