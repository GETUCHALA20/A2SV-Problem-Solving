class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for elem in tokens:
            if elem in ['*','+','-','/']:
                pop1 = stack.pop()
                pop2 = stack.pop()
                if elem == '+':
                    sum1 = pop1 + pop2
                elif elem == '*':
                    sum1 = pop1 * pop2
                elif elem == '/':
                    sum1 = int(pop2 / pop1)
                else:
                    sum1 = pop2 - pop1
                stack.append(sum1)
            else:
                stack.append(int(elem))
        return stack[0]