from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        parent_stack = []

        while curr:
            if curr.child:
                if curr.next:
                    parent_stack.append(curr.next)
                curr.child.prev = curr
                curr.next = curr.child
                curr.child = None

            if not curr.next and parent_stack:
                curr.next = parent_stack.pop()
                if curr.next:
                    curr.next.prev = curr

            curr = curr.next

        return head

        return head
