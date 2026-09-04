class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums = sorted(nums)

        for i in range(len(nums)-1, 0, -1):
            if (nums[i] - nums[i-1]) > 1:
                return nums[i-1] + 1
            elif (nums[i] - nums[i-1]) < 1:
                return nums[i] + 1
            else:
                continue

        if nums[0] == 0:
            return nums[len(nums)-1] + 1
        return 0