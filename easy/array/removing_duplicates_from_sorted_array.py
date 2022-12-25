# https://leetcode.com/explore/featured/card/top-interview-questions-easy/92/array/727/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        
        for n in range(1, len(nums)):
            if nums[n-1] != nums[n]:
                nums[i] = nums[n]
                i += 1
            
        return i
            
        
        
        