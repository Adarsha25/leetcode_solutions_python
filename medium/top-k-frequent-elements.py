#  https://leetcode.com/problems/top-k-frequent-elements/submissions/880687245/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict(collections.Counter(nums))
        heap = []
        for key, val in d.items():
            if len(heap) == k:
                heapq.heappushpop(heap, (val,key))
            else:
                heapq.heappush(heap, (val,key))
        return [y for x,y in heap]