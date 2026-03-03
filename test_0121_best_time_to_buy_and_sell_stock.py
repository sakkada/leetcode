"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

#121 Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on
the ith day.

You want to maximize your profit by choosing a single day to buy one stock and
choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot
achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit =
6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must
buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:

- 1 <= prices.length <= 10**5
- 0 <= prices[i] <= 10**4
"""

import pytest


class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     pairs = [[prices[0], None]]
    #     for index in range(1, len(prices)):
    #         i = prices[index]
    #         nopair = pairs[-1][1] is None
    #         # new item smaller then min
    #         if i < pairs[-1][0]:
    #             if nopair:
    #                 pairs[-1][0] = i
    #             else:
    #                 pairs.append([i, None])
    #                 # remote unusable pairs
    #                 if len(pairs) == 3:
    #                     if pairs[0][1] - pairs[0][0] < pairs[1][1] - pairs[1][0]:
    #                         pairs.pop(0)
    #                     else:
    #                         pairs.pop(1)
    #         # new item greater than max or max is empty yet
    #         elif nopair and i > pairs[-1][0] or not nopair and i > pairs[-1][1]:
    #             pairs[-1][1] = i
    #
    #     if len(pairs) == 2 and pairs[1][1] is not None:
    #         if pairs[0][1] - pairs[0][0] >= pairs[1][1] - pairs[1][0]:
    #             pair = pairs[0]
    #         else:
    #             pair = pairs[1]
    #     elif pairs[0][1] is not None:
    #         pair = pairs[0]
    #     else:
    #         pair = [0, 0]
    #
    #     return pair[1] - pair[0]
    #
    # def maxProfit(self, prices: List[int]) -> int:
    #     profit = 0
    #     left, right = prices[0], 0
    #     for i in prices[1:]:
    #         if i < left:
    #             left, right = i, 0
    #         elif i > right:
    #             right = i
    #         else:
    #             continue
    #         if profit < right - left:
    #             profit = right - left
    #
    #     return profit

    def maxProfit(self, prices: list[int]) -> int:
        l, r, maxp = prices[0], 0, 0
        for i in prices[1:]:
            if l > i:
                l, r = i, i
            elif r < i:
                r = i
                maxp = max(maxp, r - l)
        return maxp


config = {
    "params": [
        ({"prices": [7, 1, 5, 3, 6, 4]}, 5),
        ({"prices": [7, 6, 4, 3, 1]}, 0),
    ],
    "method": "maxProfit",
}


@pytest.mark.parametrize("input, output", config["params"])
def test_solution(input, output):
    method = config["method"]
    result = Solution().__getattribute__(method)(**input)
    assert output == result
