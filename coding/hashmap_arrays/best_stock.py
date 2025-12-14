class Solution:
    def maxProfit(self, prices):
        max_profit = 0
        min_buy = prices[0]

        for price in prices:
            max_profit = max(max_profit, price - min_buy)
            min_buy = min(min_buy, price)

        return max_profit


if __name__ == "__main__":
    sol = Solution()

    assert sol.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert sol.maxProfit([7, 6, 4, 3, 1]) == 0
    assert sol.maxProfit([1, 2]) == 1
    assert sol.maxProfit([2, 1]) == 0
    assert sol.maxProfit([3, 3, 3]) == 0

    print("All test cases passed ✅")
