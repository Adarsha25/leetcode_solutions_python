# https://leetcode.com/problems/intersection-of-two-arrays/submissions/865217770/

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(i for i in nums1 if i in nums2)
        