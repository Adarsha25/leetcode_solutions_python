# https://leetcode.com/problems/rotate-array/submissions/867602091/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k<len(nums):
            nums[0:k],nums[k:]=nums[-k:],nums[0:len(nums)-k]
        else:
            for i in range(0,k):
                nums[0],nums[1:]=nums[-1],nums[0:-1]