class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if target <= nums[0]:
                return 0
            return 1
        mid = len(nums)//2
        if target > nums[mid]:
            return mid + self.searchInsert(nums[mid:],target)
        elif target < nums[mid]:
            return self.searchInsert(nums[:mid],target)
        else:
            return mid