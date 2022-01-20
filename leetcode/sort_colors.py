class Solution(object):
    def sortColors(self, nums):
        holder = [0]*3
        for elem in nums:
            holder[elem] += 1
        prev = 0
        for i,elem in enumerate(holder):
            nums[prev:prev+elem] = [i]*elem
            prev+=elem
        return nums