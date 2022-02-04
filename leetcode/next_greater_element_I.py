class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for elem in nums1:
            index = nums2.index(elem)
            index = index + 1
            found = False
            while index < len(nums2):
                if elem < nums2[index]:
                    res.append(nums2[index])
                    found = True
                    break
                index += 1
            if not found:
                res.append(-1)
        return res