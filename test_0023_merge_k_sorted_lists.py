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
        node = self
        yield node
        while node.next:
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


node05 = ListNode(5, next=None)
node04 = ListNode(4, next=node05)
node01 = ListNode(1, next=node04)

node14 = ListNode(4, next=None)
node13 = ListNode(3, next=node14)
node11 = ListNode(1, next=node13)

node26 = ListNode(6, next=None)
node22 = ListNode(2, next=node26)

node306 = ListNode(6, next=None)
node305 = ListNode(5, next=node306)
node304 = ListNode(4, next=node305)
node314 = ListNode(4, next=node304)
node303 = ListNode(3, next=node314)
node302 = ListNode(2, next=node303)
node301 = ListNode(1, next=node302)
node311 = ListNode(1, next=node301)

node41 = ListNode(1, next=None)
node42 = ListNode(2, next=node41)

config = {
    "params": [
        ({"lists": [node01, node11, node22]}, node311),
        ({"lists": [None]}, None),
        ({"lists": [None, None, None]}, None),
        ({"lists": []}, None),
        ({"lists": [None, node41]}, node41),
    ],
    "method": "mergeKLists",
}


@pytest.mark.parametrize("input, output", config["params"])
def test_solution(input, output):
    method = config["method"]
    result = Solution().__getattribute__(method)(**input)
    assert output == result
