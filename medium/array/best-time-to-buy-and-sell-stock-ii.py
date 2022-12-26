# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/submissions/865657043/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        nums = prices
        sell = 0

        for i in range(1,len(prices)):
            if nums[i]>nums[i-1]:
                n =nums[i]-nums[i-1]
                sell += n
        return sell

