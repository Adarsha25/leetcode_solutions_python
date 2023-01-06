#  https://leetcode.com/problems/reshape-the-matrix/submissions/872668116/

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = [[0 for i in range(c)] for j in range(r)]

        row = 0
        col = 0

        if len(mat)*len(mat[0]) != r*c:
            return mat

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                m[row][col]=mat[i][j]
                col +=1

                if col == c:
                    row += 1
                    col = 0

        return m

