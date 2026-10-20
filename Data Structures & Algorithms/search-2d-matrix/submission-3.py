class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary search to find correct row
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows - 1
        found_row = -1

        while top <= bot:
            row = (top + bot) // 2

            if target < matrix[row][0]:
                bot = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                found_row = row
                break
        
        if found_row == -1: # check we found a row
            return False

        # Binary search to find target in the row
        l, r = 0, cols - 1

        while l <= r:
            m = (l + r) // 2

            if target == matrix[found_row][m]:
                return True
            elif target < matrix[found_row][m]:
                r = m - 1
            else:
                l = m + 1
        return False
        



                
        