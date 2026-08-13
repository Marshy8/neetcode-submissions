class Solution:
    def isValid(self, s: str) -> bool:
        
        mapper = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:

            if c in mapper:
                if stack:
                    topElt = stack.pop()
                else:
                    topElt = "~"
                if mapper[c] != topElt:
                    return False

            else:
                stack.append(c)

        if len(stack) > 0:
            return False

        return True
