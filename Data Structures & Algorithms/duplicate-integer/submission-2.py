class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        d = dict(zip(nums, nums))
        if len(d) < len(nums):
            return True
        return False
