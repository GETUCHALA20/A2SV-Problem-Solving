class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        res = 0
        i = len(piles)
        j = 0
        while j < i:
            j+=1
            res+=piles[i-2]
            i-=2
        return res