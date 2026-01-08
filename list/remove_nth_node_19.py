# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Step 1: Convert linked list to list of nodes (like your array)
        nodes = []
        current = head
        while current:
            nodes.append(current)
            current = current.next

        # Step 2: Calculate index to remove (N-th from end)
        index_to_remove = len(nodes) - n

        # Step 3: Remove the node
        if index_to_remove == 0:
            # Removing head
            head = head.next
        else:
            # Link previous node to next of the removed node
            prev_node = nodes[index_to_remove - 1]
            prev_node.next = prev_node.next.next

        return head
