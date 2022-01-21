class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        i = 0
        intervals = sorted(intervals,key=lambda x:x[0])
        while i < len(intervals):
            value = intervals[i]
            count = 0
            for j in range(i+1,len(intervals)):
                if  intervals[j][0] <= value[1]:
                    value = [min(intervals[j][0],value[0]),max(intervals[j][1],value[1])]
                else:
                    break
                count += 1
            res.append(value)
            i+=count+1
        return res