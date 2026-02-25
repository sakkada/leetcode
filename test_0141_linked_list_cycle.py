"""
https://leetcode.com/problems/linked-list-cycle/

#141 Linked List Cycle

Given head, the head of a linked list, determine if the linked list has a cycle
in it.

There is a cycle in a linked list if there is some node in the list that can be
reached again by continuously following the next pointer. Internally, pos is
used to denote the index of the node that tail's next pointer is connected
to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:

Input: head = [3,2,0,-4], pos = 1 (3 -> 2 -> 0 -> -4 .)
                                        ^-------------
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to
the 1st node (0-indexed).

Example 2:

Input: head = [1,2], pos = 0 (1 -> 2 .)
                              ^-------
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to
the 0th node.

Example 3:

Input: head = [1], pos = -1 (1)
Output: false
Explanation: There is no cycle in the linked list.

Constraints:

- The number of the nodes in the list is in the range [0, 104].
- -105 <= Node.val <= 105
- pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?
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
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        slow, fast = head, head
        while fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            elif not fast:
                break
        return False


N = ListNode

n11 = N(3, N(2, N(0, N(-4))))
n11.next.next.next.next = n11.next  # -4 -> 2

n21 = N(1, N(2))
n21.next.next = n21  # 2 -> 1

n31 = N(1)

config = {
    "params": [
        ({"head": n11}, True),
        ({"head": n21}, True),
        ({"head": n31}, False),
    ],
    "method": "hasCycle",
}


@pytest.mark.parametrize("input, output", config["params"])
def test_solution(input, output):
    method = config["method"]
    result = Solution().__getattribute__(method)(**input)
    assert output == result
