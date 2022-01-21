class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        distance = {}
        for i,point in enumerate(points):
            d = ((point[0])**2+(point[1])**2)
            distance[i] = d
        count = 0
        distance = dict(sorted(distance.items(), key=lambda item: item[1],reverse=False))
        for key in distance:
            if count == k:
                break
            count +=1
            res.append(points[key])
        return res