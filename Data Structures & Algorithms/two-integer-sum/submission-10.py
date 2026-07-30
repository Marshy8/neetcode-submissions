class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ordered = sorted(nums)

        print(ordered)
        for i in range(len(ordered) - 1, 0, -1):
            print("i: ", ordered[i])
            for l in range(0, i):
                print("l: ", ordered[l])
                if ordered[i] + ordered[l] > target:
                    break
                elif ordered[l] + ordered[i] == target:
                    return sorted([nums.index(ordered[l]), len(nums)-1-nums[::-1].index(ordered[i])])
                   
        return [0,0]