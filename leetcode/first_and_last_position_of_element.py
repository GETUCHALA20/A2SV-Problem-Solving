class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) <= 1:
            if len(nums) == 1 and nums[0] == target:
                return [0,0]
            return [-1,-1]
        mid = len(nums)//2
        
        if target > nums[mid]:
            return map(lambda x: x+mid if x!=-1 else x ,self.searchRange(nums[mid:],target))
        elif target < nums[mid]:
            return self.searchRange(nums[:mid],target)
        else:
            start = mid
            end = mid
            print(start,end)
            while (start>=0) and target == nums[start]:
                start-=1
            while (end < len(nums)) and target == nums[end]:
                end+=1
            return [start+1,end-1]