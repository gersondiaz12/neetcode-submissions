class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = { "}" : "{", "]" : "[", ")" : "("}
        stack = []

        l = 0

        for r in range(len(s)):
            if stack and s[r] in closeToOpen and stack[-1] == closeToOpen[s[r]]:
                stack.pop()

            else:
                stack.append(s[r])
        
        return True if not stack else False
