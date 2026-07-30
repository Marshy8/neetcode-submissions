class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = sorted(list(s))
        print(ss)
        tt = sorted(list(t))
        print(tt)
        if len(s) != len(t):
            print(1)
            return False
        for i in range(0, len(ss)):
            if ss[i] != tt[i]:
                print(2)
                return False
        print(3)
        return True
        