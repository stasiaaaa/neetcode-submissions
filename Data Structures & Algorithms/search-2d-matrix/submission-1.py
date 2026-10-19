class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix[0]) - 1
        for row in matrix:
            if target >= row[0] and target <= row[-1]:
                while l <= r:
                    m = (l + r) // 2
                    if target == row[m]:
                        return True
                    elif target > row[m]:
                        l = m + 1
                    else:
                        r = m - 1
        return False
                
        