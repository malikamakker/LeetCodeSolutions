class Solution:
    def compute(self, days: List[int], costs: List[int], last_day: int, idx: int, dp) -> int:
        if idx == len(days):
            return 0

        if days[idx] > last_day:
            if dp[idx]:
                return dp[idx]
            res = min(
                costs[0] + self.compute(days, costs, days[idx], idx + 1, dp),
                costs[1] + self.compute(days, costs, days[idx] + 6, idx + 1, dp),
                costs[2] + self.compute(days, costs, days[idx] + 29, idx + 1, dp),
            )
            dp[idx] = res
            return res
        else:
            return self.compute(days, costs, last_day, idx + 1, dp)

    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [None for _ in range(len(days))]
        return self.compute(days, costs, 0, 0, dp)
        