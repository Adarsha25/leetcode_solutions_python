#https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        res = []
        for num in nums:
           sum = sum +num
           res.append(sum)
        return res  
    