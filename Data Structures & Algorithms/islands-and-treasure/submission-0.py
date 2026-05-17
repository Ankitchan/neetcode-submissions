class Solution:

    

    def bfs(self, grid, startR, startC, M, N, dist):

        dirs = [[0, 1], [1,0], [-1, 0], [0, -1]]
        queue = deque()
        queue.append((startR, startC, dist))
        while(len(queue)) > 0:
            (r,c, currDist) = queue.popleft()


            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                # Only visit if in bounds and if the current path is shorter than existing distance
                if 0 <= nr < M and 0 <= nc < N and grid[nr][nc] > currDist + 1:
                    grid[nr][nc] = currDist + 1
                    queue.append((nr, nc, currDist + 1))

        return grid



    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        M = len(grid)
        N = len(grid[0])

        for r in range(M):
            for c in range(N):
                if grid[r][c] == 0:
                    self.bfs(grid, r, c, M, N, 0)
        