class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict(Counter(nums))     
        d= dict(sorted(d.items(), key=lambda item: item[1], reverse=True))

        return list(d)[:k]

       