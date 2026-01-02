class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        magic_grid_count = 0
        
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                subgrid = [grid[i+x][j:j+3] for x in range(3)]
                if self.isMagicGrid(subgrid):
                    magic_grid_count += 1

        return magic_grid_count


    def isMagicGrid(self, grid: List[List[int]]) -> int:
        nums = []
        for row in grid:
            for num in row:
                if num < 1 or num > 9 or num in nums:
                    return False
                nums.append(num)

        for i in range(3):
            if sum(grid[i]) != 15:
                return False
            
        for j in range(3):
            if sum(grid[i][j] for i in range(3)) != 15:
                return False
            
        if sum(grid[i][i] for i in range(3)) != 15:
            return False
        if sum(grid[i][2-i] for i in range(3)) != 15:
            return False
        
        return True