
from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #Dummy node to simplify edge cases
        dummy = ListNode(-1)
        tail = dummy
        
        #While both lists have nodes
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        #Append the remaining part of whichever list is not empty
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        
        return dummy.next
