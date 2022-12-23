# https://leetcode.com/problems/permutations/submissions/864203798/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))