# https://leetcode.com/problems/missing-number/submissions/865208443/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        N = len(nums)
        
        for i in range(N+1):
            if i not in c:
                return i

        
    