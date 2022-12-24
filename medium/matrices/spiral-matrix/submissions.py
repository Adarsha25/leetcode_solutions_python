# https://leetcode.com/problems/spiral-matrix/submissions/864885576/

class Solution:
    def spiralOrder(self, m: List[List[int]]) -> List[int]:
        res = []
        l, r = 0, len(m[0])
        t, b = 0, len(m)

        while l<r and t<b:
            # top row
            for i in range(l, r):
                res.append(m[t][i])
            t +=1
            
            # right column
            for i in range(t, b):
                res.append(m[i][r-1])
            r -= 1

            if not (l<r and t<b):
                break
            
            # bottom row
            for i in range(r-1, l-1, -1):
                res.append(m[b-1][i])
            b -=1

            # left column
            for i in range(b-1, t-1, -1):
                res.append(m[i][l])
            l +=1

        return res 