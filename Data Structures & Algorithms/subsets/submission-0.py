import itertools

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        l = []

        for i in range(len(nums)+1):
            for sub in itertools.combinations(nums, i):
                l.append(list(sub))

        return l