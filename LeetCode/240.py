from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        col = 0
        row_count = len(matrix)

        try:
            while True:
                if matrix[row][col] == target:
                    return True

                elif matrix[row][col] < target:
                    row += 1
                    if row == row_count:
                        row = 0
                        col += 1
                        if matrix[row][col] > target:
                            return False

                else:
                    row = 0
                    col += 1
                    if matrix[row][col] > target:
                        return False

        except IndexError:
            return False
