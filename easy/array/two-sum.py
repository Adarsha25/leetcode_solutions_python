# https://leetcode.com/problems/two-sum/submissions/868181233/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, j in enumerate(nums):
            rem = target - j
            if rem in dic:
                return [dic[rem], i]
            dic[j] = i