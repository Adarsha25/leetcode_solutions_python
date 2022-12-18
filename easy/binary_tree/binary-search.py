# https://leetcode.com/problems/binary-search/submissions/861655887/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start,end = 0,len(nums)-1
        while start<=end:
            m = (start+end)//2
            if nums[m] > target:
                end = m-1
            elif nums[m]< target:
                start = m+1
            else:
                return m
        return -1