# https://leetcode.com/problems/permutations/submissions/864203798/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def inner(input_word, taken=[]):
            if len(input_word) == 0:
                answer.append(taken)
                return
            for idx in range(len(input_word)):
                inner(input_word[:idx] + input_word[idx + 1:], taken + [input_word[idx]])

        inner(nums)
        return answer