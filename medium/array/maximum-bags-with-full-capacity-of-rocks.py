# https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/submissions/

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        c = capacity

        for i in range(n):
            c[i] -= rocks[i]
        c.sort()

        for i in range(n):
            if c[i] != 0:
                if c[i] > additionalRocks:
                    return i 
                else:
                    additionalRocks -= c[i]
        return n

                
        

        