"""
https://leetcode.com/problems/reverse-linked-list/

#206 Reverse Linked List

Given the head of a singly linked list, reverse the list, and return the
reversed list.

Example 1:

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:

Input: head = [1,2]
Output: [2,1]

Example 3:

Input: head = []
Output: []

Constraints:

- The number of nodes in the list is the range [0, 5000].
- -5000 <= Node.val <= 5000

Follow up: A linked list can be reversed either iteratively or recursively.
Could you implement both?
"""

import pytest


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode|None" = None):
        self.val: int = val
        self.next: "ListNode|None" = next

    def __str__(self):
        return f"LL({' '.join(str(i.val) for i in self.as_list())})"

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other) -> bool:
        if not isinstance(other, ListNode):
            return False
        return self.val == other.val

    def as_list(self):
        visited: set[int] = set()
        node = self
        yield node
        while node.next:
            if id(node.next) in visited:
                yield ListNode(node.next.val * 100000)
                break
            visited.add(id(node.next))
            yield node.next
            node = node.next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr, next = None, None, head
        while next:
            curr, next = next, next.next
            curr.next, prev = prev, curr

        return curr


N = ListNode

config = {
    "params": [
        ({"head": N(1, N(2, N(3, N(4, N(5)))))}, N(5, N(4, N(3, N(2, N(1)))))),
        ({"head": N(1, N(2))}, N(2, N(1))),
        ({"head": N(1)}, N(1)),
        ({"head": None}, None),
    ],
    "method": "reverseList",
}


@pytest.mark.parametrize("input, output", config["params"])
def test_solution(input, output):
    method = config["method"]
    result = Solution().__getattribute__(method)(**input)
    assert output == result
