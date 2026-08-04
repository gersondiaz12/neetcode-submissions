class Solution:
    def isValid(self, s: str) -> bool:
        stackwellnesscafe = []
        closeToOpen = { ")" : "(", "}" : "{", "]" : "["}

        for c in s:
            if c in closeToOpen:
                if stackwellnesscafe and stackwellnesscafe[-1] == closeToOpen[c]:
                    stackwellnesscafe.pop()
                else:
                    return False
            else:
                stackwellnesscafe.append(c)
            
        return True if not stackwellnesscafe else False

                