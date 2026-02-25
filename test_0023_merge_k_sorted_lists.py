"""
https://leetcode.com/problems/merge-k-sorted-lists/

#23 Merge k Sorted Lists

You are given an array of k linked-lists lists, each linked-list is sorted in
ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked list:
1->1->2->3->4->4->5->6

Example 2:

Input: lists = []
Output: []

Example 3:

Input: lists = [[]]
Output: []

Constraints:

- k == lists.length
- 0 <= k <= 104
- 0 <= lists[i].length <= 500
- -104 <= lists[i][j] <= 104
- lists[i] is sorted in ascending order.
- The sum of lists[i].length will not exceed 104.
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
    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = node = ListNode()
        while l1 and l2:
            if l1.val <= l2.val:
                node.next, l1 = l1, l1.next
            else:
                node.next, l2 = l2, l2.next
            node, node.next = node.next, None

            if not l1:
                node.next = l2
            elif not l2:
                node.next = l1

        return head.next

    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        if not lists or len(lists) == 1:
            return lists[0] if lists else None
        lidx, left = next(((idx, i) for idx, i in enumerate(lists) if i), (None, None))
        if left is None:
            return None

        for idx in range(lidx + 1, len(lists)):
            right = lists[idx]
            if right:
                left = self.merge(left, right)
        return left


N = ListNode

config = {
    "params": [
        (
            {"lists": [N(1, N(4, N(5))), N(1, N(3, N(4))), N(2, N(6))]},
            N(1, N(1, N(2, N(3, N(4, N(4, N(5, N(6)))))))),
        ),
        ({"lists": [None]}, None),
        ({"lists": [None, None, None]}, None),
        ({"lists": []}, None),
        (
            {"lists": [None, N(1, N(2))]},
            N(1, N(2)),
        ),
    ],
    "method": "mergeKLists",
}


@pytest.mark.parametrize("input, output", config["params"])
def test_solution(input, output):
    method = config["method"]
    result = Solution().__getattribute__(method)(**input)
    assert output == result
