class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_len = 1
        result = s[0]
        dp = [[None for _ in range(len(s))] for _ in range(len(s))]

        for _len in range(len(s)):
            for i in range(len(s) - _len):
                if _len == 0:
                    dp[i][i] = True
                else:
                    l, r = i, i+_len
                    if r < len(s):
                        inner_l, inner_r = l + 1, r - 1
                        inner_palindrome = True
                        if inner_l <= inner_r:
                            inner_palindrome = dp[inner_l][inner_r]
                        if inner_palindrome and s[l] == s[r]:
                            dp[l][r] = True
                            if (r-l+1) > max_len:
                                result = s[l:r+1]
                                max_len = r-l+1 
                        else:
                            dp[l][r] = False
        return result
        