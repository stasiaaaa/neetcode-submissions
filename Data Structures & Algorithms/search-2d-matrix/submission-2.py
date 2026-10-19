class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # binary to find the right row 
        rows, cols = len(matrix), len(matrix[0])
        # no. of rows 
        top, bot = 0, rows - 1
        found_row = -1

        while top <= bot:
            row = (top + bot) // 2
            if target < matrix[row][0]:
                bot = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else: # we found the row
                found_row = row
                break
        # Check we found row
        if found_row == -1:
            return False

        # binary to find the target in the row
        l, r = 0, cols - 1
        while l <= r:
            m = (l + r) // 2
            if target == matrix[found_row][m]:
                return True
            elif target > matrix[found_row][m]:
                l = m + 1
            else:
                r = m - 1
        return False

                
        