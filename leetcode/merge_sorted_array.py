class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i,j,k = 0,0,0
        while i < len(nums1) and j < n:
            if (k >= m and nums1[i] == 0) or (len(nums1)==n) or nums1[i] > nums2[j]:
                nums1.insert(i,nums2[j])
                nums1.pop()
                i+=1
                j+=1
            else:
                i+=1
                k+=1