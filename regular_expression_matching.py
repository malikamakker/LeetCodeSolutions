class Solution:
    def match(self, s: str, p: str, s_idx: int, p_idx: int, dp) -> bool:
        if s_idx == len(s) and p_idx == len(p):
            return True
        elif p_idx == len(p):
            return False
        elif s_idx > len(s):
            return False
        
        if s_idx < len(s) and dp[s_idx][p_idx] is not None:
            return dp[s_idx][p_idx]
        
        result = False
        if p[p_idx] == '*':
            preceding = p[p_idx-1]
            if preceding == '.':
                result =  self.match(s, p, s_idx+1, p_idx, dp) or self.match(s, p, s_idx+1, p_idx + 1, dp) or self.match(s, p, s_idx, p_idx+1, dp)
            elif s_idx < len(s) and s[s_idx] == preceding:
                result = self.match(s, p, s_idx+1, p_idx, dp) or self.match(s, p, s_idx+1, p_idx+1, dp) or self.match(s, p, s_idx, p_idx+1, dp)
            else:
                result = self.match(s, p, s_idx, p_idx+1, dp)
        
        elif p[p_idx] == '.':
            result = self.match(s, p, s_idx+1, p_idx+1, dp)
            if (p_idx+1) < len(p) and p[p_idx + 1] == '*':
                result = self.match(s, p, s_idx, p_idx+1, dp) or result
        
        else:
            if s_idx < len(s) and p[p_idx] == s[s_idx]:
                result = self.match(s, p, s_idx+1, p_idx+1, dp)
            if (p_idx+1) < len(p) and p[p_idx + 1] == '*':
                result = self.match(s, p, s_idx, p_idx+1, dp) or result
        
        if s_idx < len(s):
            dp[s_idx][p_idx] = result
        return result

    def isMatch(self, s: str, p: str) -> bool:
        dp = [[None for _ in range(len(p))] for _ in range(len(s))]
        return self.match(s, p, 0, 0, dp)
        