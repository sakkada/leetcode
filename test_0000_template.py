"""
https://leetcode.com/problems/{{problem_slug}}/

#{{problem_number}} {{problem_name}}

{{problem_text}}
"""

import pytest


class Solution:
    def {{problem_method_name}}(self, {{input_args}}) -> {{output_type}}:
        ...


config = {
    "params": [
        ({{input}}, {{output}}),
    ],
    "method": "{{problem_method_name}}",
}


@pytest.mark.parametrize("input, output", config["params"])
def test_solution(input, output):
    method = config["method"]
    result = Solution().__getattribute__(method)(**input)
    assert output == result
