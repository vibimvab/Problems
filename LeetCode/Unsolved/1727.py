from typing import List

class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        row_count = len(matrix)
        col_count = len(matrix[0])

        lengths = [[0 for _ in range(row_count)] for _ in range(row_count)]
        for col in range(col_count):
            for row_start in range(row_count):
                for row_end in range(row_start, row_count):
                    if matrix[row_end][col] == 0:
                        break
                    lengths[row_start][row_end] += 1

        area = -1
        for left in range(row_count):
            for right in range(left, row_count):
                area = max(area, (right - left + 1) * lengths[left][right])

        return area


if __name__ == '__main__':
    edge_case = [[1 for _ in range(20)] for _ in range(5000)]
    s = Solution()
    print(s.largestSubmatrix([[1 for _ in range(20)] for _ in range(5000)]))
    