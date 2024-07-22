class Solution:
    def traverse(self, s: str, p: str, s_idx: int, p_idx:int, dp):
        if s_idx == len(s) and p_idx == len(p):
            return True
        elif s_idx == len(s) and p[p_idx] == '*':
            return self.traverse(s, p, s_idx, p_idx+1, dp)
        elif s_idx == len(s) or p_idx == len(p):
            return False
        
        if dp[s_idx][p_idx] is not None:
            return dp[s_idx][p_idx]

        result = False

        if p[p_idx] == '*':
            result = self.traverse(s, p, s_idx + 1, p_idx + 1, dp) or self.traverse(s, p, s_idx+1, p_idx, dp) or self.traverse(s, p, s_idx, p_idx + 1, dp)
        elif p[p_idx] == '?':
            result = self.traverse(s, p, s_idx+1, p_idx+1, dp)
        elif p[p_idx] == s[s_idx]:
            result = self.traverse(s, p, s_idx+1, p_idx+1, dp)
        
        dp[s_idx][p_idx] = result
        return result


    def isMatch(self, s: str, p: str) -> bool:
        dp = [[None for _ in range(len(p))] for _ in range(len(s))]
        return self.traverse(s, p, 0, 0, dp)
        