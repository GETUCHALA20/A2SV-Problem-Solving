class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        sum_closest_to_target = float("inf")
        length = len(nums) - 1
        for i in range(0, len(nums)-2):
            j = i + 1
            k = length
            
            while j < k:
                sum1 = nums[i] + nums[j] + nums[k]
                distance = abs(target-sum1)
                
                if distance < abs(target-sum_closest_to_target):
                    sum_closest_to_target = sum1
                    
                if sum1 < target:
                    j += 1
                else:
                    k -= 1
                    
        return sum_closest_to_target