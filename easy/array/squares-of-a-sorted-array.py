# https://leetcode.com/problems/squares-of-a-sorted-array/submissions/863795048/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        A = []
        for x in nums:
            x= x**2
            A.append(x)
            A.sort()
        return A