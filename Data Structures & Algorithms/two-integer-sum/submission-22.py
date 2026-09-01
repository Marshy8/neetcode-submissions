class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sort = sorted(nums)
        

        left = 0
        right = len(nums) - 1

        while (sort[left] + sort[right]) != target:
            if (sort[left] + sort[right]) > target:
                right -= 1
            elif (sort[left] + sort[right]) < target:
                left += 1

        output = sorted([nums.index(sort[left]), len(nums)-1-nums[::-1].index(sort[right])])

        return output