class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = []
        for i,elem in enumerate(temperatures):
            if len(stack) == 0:
                stack.append((elem,i))
                res.append(0)
            else:
                while stack and stack[-1][0] < elem:
                    pop = stack.pop()
                    res[pop[1]]+= (i-pop[1])
                stack.append((elem,i))
                res.append(0)
        return res