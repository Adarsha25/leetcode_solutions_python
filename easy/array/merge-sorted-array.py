# https://leetcode.com/problems/merge-sorted-array/submissions/868196767/?envType=study-plan&id=data-structure-i

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:n]
        nums1.sort()