from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        num_str = sorted(map(str,nums),key=cmp_to_key(lambda x, y: 1 if x+y < y+x else -1))
        res = "".join(num_str)
        if res[0] == "0":
            return "0" 
        else:
            return res