class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        rpnStack= []
        res = 0

        for t in tokens:
            if t == '+':
                rpnStack.append(rpnStack.pop() + rpnStack.pop())
            elif t == '-':
                a, b = rpnStack.pop(), rpnStack.pop()
                rpnStack.append(b - a)
            elif t == '*':
                rpnStack.append(rpnStack.pop() * rpnStack.pop())
            elif t == '/':
                a, b = rpnStack.pop(), rpnStack.pop()
                rpnStack.append(int(b / a))
            else:
                rpnStack.append(int(t))
        
        return rpnStack[0]