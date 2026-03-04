"""
https://leetcode.com/problems/product-of-array-except-self/

#238 Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is
equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit
integer.

You must write an algorithm that runs in O(n) time and without using the
division operation.

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:

- 2 <= nums.length <= 10**5
- -30 <= nums[i] <= 30

The input is generated such that answer[i] is guaranteed to fit in a 32-bit
integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The
output array does not count as extra space for space complexity analysis.)
"""

import pytest


class Solution:
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     # prepare precalculated lists (above and below diagonal)
    #     ln = len(nums)
    #     a, b = list([1] * ln), list([1] * ln)
    #
    #     # calculate precalculated lists
    #     for i in range(1, ln):
    #         a[i] = a[i - 1] * nums[i - 1]
    #     for i in range(ln - 2, -1, -1):
    #         b[i] = b[i + 1] * nums[i + 1]
    #
    #     # combine result
    #     c = [i * j for i, j in zip(a, b)]
    #
    #     return c
    #
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     # prepare precalculated lists (above and below diagonal)
    #     ln = len(nums)
    #     a, b = list([1] * ln), list([1] * ln)
    #
    #     # calculate precalculated lists
    #     for l in range(1, ln):
    #         r = ln - l - 1
    #         a[l] = a[l - 1] * nums[l - 1]
    #         b[r] = b[r + 1] * nums[r + 1]
    #
    #     # combine result
    #     c = [i * j for i, j in zip(a, b)]
    #
    #     return c

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # O(n) time O(1) space (output array does not count as extra space)
        ln = len(nums)
        nm = [0] * ln
        for i in range(ln):
            nm[i] = nm[i - 1] * nums[i - 1] if i else 1

        tail = 1
        for i in range(ln - 1, -1, -1):
            nm[i] *= tail
            tail *= nums[i]

        return nm


config = {
    "params": [
        ({"nums": [1, 2, 3, 4]}, [24, 12, 8, 6]),
        ({"nums": [-1, 1, 0, -3, 3]}, [0, 0, 9, 0, 0]),
    ],
    "method": "productExceptSelf",
}


@pytest.mark.parametrize("input, output", config["params"])
def test_solution(input, output):
    method = config["method"]
    result = Solution().__getattribute__(method)(**input)
    assert output == result
