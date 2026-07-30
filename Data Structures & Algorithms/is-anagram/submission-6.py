class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = sorted(list(s))
        tt = sorted(list(t))

        if len(s) != len(t):
            return False
        for i in range(0, len(ss)):
            if ss[i] != tt[i]:
                return False
        return True
        