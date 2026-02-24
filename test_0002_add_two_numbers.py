"""
https://leetcode.com/problems/add-two-numbers/

#2 Add Two Numbers

You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order, and each of their nodes
contains a single digit. Add the two numbers and return the sum as a linked
list.

You may assume the two numbers do not contain any leading zero, except the
number 0 itself.

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

- The number of nodes in each linked list is in the range [1, 100].
- 0 <= Node.val <= 9
- It is guaranteed that the list represents a number that does not have leading
  zeros.
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
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = node = ListNode()
        tens = 0
        while l1 or l2:
            units = (l1.val if l1 else 0) + (l2.val if l2 else 0) + tens
            if units > 9:
                tens, units = 1, units % 10
            else:
                tens = 0

            node.next = ListNode(units)
            node = node.next

            l1 = l1.next if l1 and l1.next else None
            l2 = l2.next if l2 and l2.next else None

            if not (l1 or l2) and tens:
                node.next = ListNode(tens)

        return head.next


l11 = ListNode(2, ListNode(4, ListNode(3)))
l12 = ListNode(5, ListNode(6, ListNode(4)))
l13 = ListNode(7, ListNode(0, ListNode(8)))

l21 = ListNode(0)
l22 = ListNode(0)
l23 = ListNode(0)

l31 = ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9, ListNode(9)))))))
l32 = ListNode(9, ListNode(9, ListNode(9, ListNode(9))))
l33 = ListNode(8, ListNode(9, ListNode(9, ListNode(9, ListNode(0, ListNode(0, ListNode(0, ListNode(1))))))))

config = {
    "params": [
        ({"l1": l11, "l2": l12}, l13),
        ({"l1": l21, "l2": l22}, l23),
        ({"l1": l31, "l2": l32}, l33),
    ],
    "method": "addTwoNumbers",
}


@pytest.mark.parametrize("input, output", config["params"])
def test_solution(input, output):
    method = config["method"]
    result = Solution().__getattribute__(method)(**input)
    assert output == result
