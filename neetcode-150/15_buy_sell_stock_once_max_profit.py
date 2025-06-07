class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 0
        sell = 1
        while sell < len(prices):  # we need to sell to achieve profit
            curr_profit = prices[sell] - prices[buy]
            if curr_profit < 0: #Update buy and sell prices
                buy = sell
                sell = buy + 1
            else:
                profit = max(profit, curr_profit)  # Update profit if current profit is greater
                sell += 1
        return profit

    # Here we are finding the min value to buy and if current value is not min value update the profit
    def maxProfit_2(self, prices: List[int]) -> int:
        min = prices[0] #Assume first price is min
        profit = 0
        for price in prices:
            if price < min:
                min = price
            else:
                profit = max(profit, price - min)
        return profit
