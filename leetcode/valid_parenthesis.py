class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {']':'[',')':'(','}':'{'}
        if string == '':
            return True
        for elem in s:
            if elem in '{[(':
                stack.append(elem)
            elif elem in '}])':
                if stack:
                    if d[elem] == stack[-1]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return True if len(stack) == 0 else False