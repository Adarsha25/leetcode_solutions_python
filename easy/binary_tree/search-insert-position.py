# https://leetcode.com/problems/search-insert-position/submissions/863603550

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        l,r = 0, len(nums)-1

        while l <= r:
            mid = r+l // 2
            if nums[mid] == target:
                return mid            
            if nums[mid] > target:
                r = mid - 1

            else:
                l = mid + 1

        if nums[mid] > target:
            return mid
        else:
            return mid + 1 