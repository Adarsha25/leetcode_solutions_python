# https://leetcode.com/problems/maximum-subarray/submissions/861616017/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray = nums[0]
        curSum = 0
        
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            max_subarray = max(max_subarray, curSum)
        return max_subarray