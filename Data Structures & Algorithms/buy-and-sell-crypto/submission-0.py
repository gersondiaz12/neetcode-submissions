class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxProfit = max(maxProfit, profit)
            else:
                l = r
            
            r += 1

        return maxProfit

# what i didn't understand:
    #
# what i learned:
    # initialize a left pointer on day 1, and a right pointer on day 2
    # find the current profit (r-l), if right > left, increment left
    # keep track of the current max profit
    # if right < left, keep left and increment right


        