class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) <= 1:
            return []
        if len(changed) % 2 != 0:
            return []
        d = {}
        res = []
        changed.sort()
        for elem in (changed):
            if elem in d:
                d[elem] += 1
            else:
                d[elem] = 1
                
        for elem in changed:
            if d[elem] == 0:
                continue
            if elem == 0:
                if d[elem] % 2 == 0:
                    res.append(elem)
                    d[elem]-=2
                else:
                    return []
            else:
                div = elem*2
                if div in d and d[div] > 0:
                    d[elem]-=1
                    d[div]-=1
                    res.append(elem)
                else:
                    return []
        return res