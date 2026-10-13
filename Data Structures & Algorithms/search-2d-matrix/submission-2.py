class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=None
        for i in range(len(matrix)):
            if matrix[i][0]<=target and matrix[i][-1]>=target:
                row=i
                break
        if row==None:
            return False
        for j in matrix[row]:
            if j==target:
                return True
        return False
        