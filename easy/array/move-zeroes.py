# https://leetcode.com/problems/move-zeroes/submissions/864276563/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nonZeroIndex = 0
        for currIndex in range(len(nums)):
            if nums[currIndex] != 0:
                if nonZeroIndex < currIndex:
                    nums[nonZeroIndex] = nums[currIndex]
                    nums[currIndex] = 0
                nonZeroIndex += 1