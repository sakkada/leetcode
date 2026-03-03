"""
https://leetcode.com/problems/contains-duplicate/

#217 Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in
the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]
Output: false
Explanation:
All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:

- 1 <= nums.length <= 10**5
- -10**9 <= nums[i] <= 10**9
"""

import pytest


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        cont = set()
        for i in nums:
            if i in cont:
                return True
            cont.add(i)
        return False


config = {
    "params": [
        ({"nums": [1, 2, 3, 1]}, True),
        ({"nums": [1, 2, 3, 4]}, False),
        ({"nums": [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]}, True),
    ],
    "method": "containsDuplicate",
}


@pytest.mark.parametrize("input, output", config["params"])
def test_solution(input, output):
    method = config["method"]
    result = Solution().__getattribute__(method)(**input)
    assert output == result
