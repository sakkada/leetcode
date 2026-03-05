"""
https://leetcode.com/problems/maximum-product-subarray/

#152 Maximum Product Subarray

Given an integer array nums, find a subarray that has the largest product, and
return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

Note that the product of an array with a single element is the value of that
element.

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Constraints:

- 1 <= nums.length <= 2 * 10**4
- -10 <= nums[i] <= 10
- The product of any subarray of nums is guaranteed to fit in a 32-bit integer.
"""

import pytest
import math


class Solution:
    # def maxProduct(self, nums: list[int]) -> int:
    #     # Drop on every zero, calculate left and right even negatives if
    #     # total amount of negatives is odd
    #     prodmax = -99
    #     ln = len(nums)
    #
    #     prod, prodln, prodrn, cneg, start = None, -99, None, 0, True
    #     for i, v in enumerate(nums):
    #         if v == 0:
    #             prod, prodln, prodrn, cneg, start = None, -99, None, 0, True
    #             prodmax = max(prodmax, 0)
    #             continue
    #
    #         if start:
    #             start = False
    #             prodmax = max(prodmax, v)
    #             prod = v
    #             cneg = 1 if v < 0 else 0
    #             continue
    #
    #         if cneg:
    #             prodrn = v if prodrn is None else prodrn * v
    #
    #         if v < 0:
    #             cneg += 1
    #             if cneg % 2:
    #                 prodln = prod
    #
    #         prod *= v
    #         prodmax = max(prodmax, prod)
    #
    #         if cneg % 2 and (i == ln - 1 or nums[i + 1] == 0):
    #             prodmax = max(prodmax, max(prodln, -99 if prodrn is None else prodrn))
    #
    #     return prodmax
    #
    # def maxProduct(self, nums: list[int]) -> int:
    #     # Elegant but hard to reimplement from memory
    #     resval = minval = maxval = nums[0]
    #     for i in nums[1:]:
    #         if i < 0:
    #             minval, maxval = maxval, minval
    #
    #         minval = min(i, i * minval)
    #         maxval = max(i, i * maxval)
    #         resval = max(resval, maxval)
    #
    #     return resval

    def maxProduct(self, nums: list[int]) -> int:
        # Bidirectional Kadane's similar algorithm
        resval = -math.inf

        prod = 1
        for i in nums:
            prod *= i
            resval = max(prod, resval)
            if prod == 0:
                prod = 1

        prod = 1
        for i in nums[::-1]:
            prod *= i
            resval = max(prod, resval)
            if prod == 0:
                prod = 1

        return resval


config = {
    "params": [
        ({"nums": [2, 3, -2, 4]}, 6),
        ({"nums": [-2, 0, -1]}, 0),
        ({"nums": [3, -1, 4]}, 4),
        ({"nums": [-1, -2, -3, 0]}, 6),
        ({"nums": [-1, 1, 2, 1]}, 2),
        ({"nums": [2, -3, 4, -5, 6, -7, 8, -2, 2]}, 161280),
        ({"nums": [-1, 2, -3, 4, -5, 6, -7, 8, -2, 2]}, 161280),
    ],
    "method": "maxProduct",
}


@pytest.mark.parametrize("input, output", config["params"])
def test_solution(input, output):
    method = config["method"]
    result = Solution().__getattribute__(method)(**input)
    assert output == result
