class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ordS = {}
        for i in range(len(strs)):
            key = "".join(sorted(strs[i]))
            if key not in ordS:
                ordS[key] = []
            ordS[key].append(strs[i])

        return list(ordS.values())