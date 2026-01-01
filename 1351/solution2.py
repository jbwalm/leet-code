class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        sum: int = 0

        row, col = 0, n - 1

        while row < m and col >= 0:
            if grid[row][col] < 0:
                sum += (m - row)
                col -= 1
            else:
                row += 1

        return sum