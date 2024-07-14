class Solution:
    def traverse(self, matrix, dp, i, j):
        if dp[i][j] is not None:
            return dp[i][j]

        accepted_i_range = range(len(matrix))
        accepted_j_range = range(len(matrix[0]))
        visited_paths = []
        existing_val = matrix[i][j]

        to_visit = [(i, j-1), (i, j+1), (i-1, j), (i+1, j)]
        not_visited = []

        for m,n in to_visit:
            if m in accepted_i_range and n in accepted_j_range:
                if matrix[m][n] > existing_val:
                    self.traverse(matrix, dp, m, n)
                    visited_paths.append(dp[m][n])
                else:
                    not_visited.append((m,n))
        
        forward = max(visited_paths) if visited_paths else 0
        dp[i][j] = forward + 1

        for m,n in not_visited:
            self.traverse(matrix, dp, m, n)

    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = [[None for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        self.traverse(matrix, dp, 0, 0)
        max_path = 0
        for i in range(len(matrix)):
            max_row = max(dp[i])
            max_path = max(max_path, max_row)
        return max_path
        