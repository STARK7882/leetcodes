class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n=len(matrix[0])
        for i in range(len(matrix)):
            for j in range(n):
                if target==matrix[i][j]:
                    return True
        return False