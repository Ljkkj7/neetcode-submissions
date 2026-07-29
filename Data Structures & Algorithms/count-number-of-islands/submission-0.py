class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        def sink(sr, sc):
            stack = [(sr, sc)]
            while stack:
                r, c = stack.pop()
                if 0 <= r < rows and 0 <= c < cols and grid[r][c] == '1':
                    grid[r][c] = '0'
                    stack.extend([(r+1, c), (r-1, c), (r, c+1), (r, c-1)])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    sink(r, c)

        return count