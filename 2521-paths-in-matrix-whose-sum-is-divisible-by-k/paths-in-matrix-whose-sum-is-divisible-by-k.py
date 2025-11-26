class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        MOD = 10**9 + 7
        rows, cols = len(grid), len(grid[0])
        
        dp = [[[0] * k for _ in range(cols)] for _ in range(rows)]
        dp[0][0][grid[0][0] % k] = 1

        for i in range(rows):
            for j in range(cols):
                for rem in range(k):
                    val = grid[i][j]
                    if i > 0:
                        dp[i][j][(rem + val) % k] += dp[i-1][j][rem]
                    if j > 0:
                        dp[i][j][(rem + val) % k] += dp[i][j-1][rem]
                    dp[i][j][(rem + val) % k] %= MOD

        return dp[rows-1][cols-1][0]