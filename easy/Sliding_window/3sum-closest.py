#  https://leetcode.com/problems/3sum-closest/submissions/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        ans = nums[0] + nums[1] + nums[2]
        for i in range(n-2):
            l, r = i + 1, n - 1
            while l < r:
                sum3 = nums[i] + nums[l] + nums[r]
                if abs(ans - target) > abs(sum3 - target):
                    ans = sum3
                if sum3 == target: return target
                if sum3 > target:
                    r -= 1  # Sum3 is greater than the target, to minimize the difference, we have to decrease our sum3
                else:
                    l += 1  # Sum3 is lesser than the target, to minimize the difference, we have to increase our sum3
        return ans
        