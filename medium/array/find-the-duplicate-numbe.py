# https://leetcode.com/problems/find-the-duplicate-number/submissions/865636709/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        s = set(nums)
        return (sum(nums)-sum(s))//(len(nums)-len(s))
        