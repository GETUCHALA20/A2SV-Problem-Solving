class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = {}
        for elem in arr:
            if elem in d:
                d[elem]+=1
            else:
                d[elem]=1
        
        d = dict(sorted(d.items(), key=lambda item: item[1],reverse=True))
        count = 0
        values = 0
        length = len(arr)
        for key in d:
            count +=1
            values += d[key]
            if values >= length//2:
                break
        return count