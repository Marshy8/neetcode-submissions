class Solution:
    def search(self, nums: List[int], target: int) -> int:
    
        lm = 0
        rm = len(nums) - 1
        mid = math.ceil((lm+rm)/2)

        while lm <= rm:
            if nums[mid] < target:
                lm = mid + 1
                mid = math.ceil((lm+rm)/2)
            elif nums[mid] > target:
                rm = mid - 1
                mid = math.ceil((lm+rm)/2)
            else:
                return mid

        return -1