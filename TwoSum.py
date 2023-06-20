class Solution(object):
    def twoSum(self, nums, target):
        for n in range(len(nums)):
            for y in range(n + 1, len(nums)):
                if (n != y and nums[n] + nums[y] == target):
                    return[n, y]
        return []