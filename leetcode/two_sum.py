class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, elem in enumerate(nums):
            d[elem]=i
        for j,elem in enumerate(nums):
            if (target - elem) in d and d[target-elem] != j:
                return [j,d[target-elem]]
        return []