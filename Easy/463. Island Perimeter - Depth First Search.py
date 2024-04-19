class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        island_total = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    island_total += 4

                    if j < len(grid[i]) - 1 and grid[i][j+1] == 1:
                        island_total -= 2

                    if i < len(grid) - 1 and grid[i+1][j] == 1:
                        island_total -= 2

        return island_total


solution = Solution()
print(solution.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))
print(solution.islandPerimeter([[1]]))
print(solution.islandPerimeter([[1,0]]))
print(solution.islandPerimeter([[0, 1]]))