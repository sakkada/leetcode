"""
https://leetcode.com/problems/maximum-subarray/

#53 Maximum Subarray

Given an integer array nums, find the subarray with the largest sum, and return
its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

Constraints:

- 1 <= nums.length <= 10**5
- -10**4 <= nums[i] <= 10**4

Follow up: If you have figured out the O(n) solution, try coding another
solution using the divide and conquer approach, which is more subtle.
"""

import pytest


class Solution:
    # # direct solution O(n^2)
    # def maxSubArray(self, nums: List[int]) -> int:
    #     ms = -999999
    #     for i in range(len(nums)):
    #         s = 0
    #         for j in range(i, -1, -1):
    #             s += nums[j]
    #             if ms < s:
    #                 ms = s
    #     return ms
    #
    # # O(n)
    # def maxSubArray(self, nums: List[int]) -> int:
    #     maxsum = nums[0]
    #     sublist, sublistsum = nums[:1], nums[0]
    #
    #     for v in nums[1:]:
    #         if sublistsum + v < v:
    #             sublist = [v]
    #             sublistsum = v
    #         else:
    #             sublist.append(v)
    #             sublistsum += v
    #         if maxsum < sublistsum:
    #             maxsum = sublistsum
    #
    #     return maxsum

    # o(n) without sublist at all
    def maxSubArray(self, nums: list[int]) -> int:
        msum, csum = nums[0], nums[0]
        for i in nums[1:]:
            if csum + i <= i:
                csum = i
            else:
                csum += i
            msum = max(msum, csum)
        return msum


config = {
    "params": [
        ({"nums": [-2, 1, -3, 4, -1, 2, 1, -5, 4]}, 6),
        ({"nums": [1]}, 1),
        ({"nums": [5, 4, -1, 7, 8]}, 23),
    ],
    "method": "maxSubArray",
}


@pytest.mark.parametrize("input, output", config["params"])
def test_solution(input, output):
    method = config["method"]
    result = Solution().__getattribute__(method)(**input)
    assert output == result
