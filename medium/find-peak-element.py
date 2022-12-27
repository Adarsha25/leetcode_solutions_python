# https://leetcode.com/problems/find-peak-element/submissions/

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        num = nums.copy()
        s = num.sort()
        res = num[len(num)-1]
        n = nums.index(res)
        return n

