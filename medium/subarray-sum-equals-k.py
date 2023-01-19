#  https://leetcode.com/problems/subarray-sum-equals-k/submissions/881355961/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans, n = 0, len(nums)
        preSum = [nums[0]]
        dic = {}
        dic[0] = 1
        for i in nums[1:]:
            preSum.append(i+preSum[-1])
        for i in preSum:
            if i-k in dic:
                ans+=dic[i-k]
            dic[i] = dic.get(i,0) + 1 
        return ans