class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit_left_array = []
        min_left = float('inf')
        max_profit_left = 0
        idx = 0

        for price in prices: 
            if idx == 0:
                min_left = price
                max_profit_left_array.append(0)
            else:
                max_profit_left = max(max_profit_left, price - min_left)
                min_left = min(price, min_left)
                max_profit_left_array.append(max_profit_left)
            idx = idx + 1

        max_right = 0
        max_profit_right = 0
        max_profit = 0
        idx = len(prices)
        for price in reversed(prices):
            max_profit_right = max(max_profit_right, max_right - price) if idx < len(prices) else 0
            max_right = max(max_right, price)
            max_profit = max(max_profit, max_profit_right+max_profit_left_array[idx-1]) if idx > 0 else max(max_profit, max_profit_right)
            idx = idx - 1
        return max_profit 
        