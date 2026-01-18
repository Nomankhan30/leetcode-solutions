//sol is in typescript
/**
 
 * Definition for singly-linked list.Provided by leetcode*/
  class ListNode {
      val: number
      next: ListNode | null
      constructor(val?: number, next?: ListNode | null) {
          this.val = (val===undefined ? 0 : val)
          this.next = (next===undefined ? null : next)
      }
  }

function hasCycle(head: ListNode | null): boolean {
    //can have ListNode reference or null, depends on value of head
    let slow: ListNode | null = head;
    let fast: ListNode | null = head;

    while (fast !== null && fast.next !== null) {
        //! Non-Null Assertion Operator in TypeScript.
        //it is ensuring the compiler, slow here is not null cause slow can either have listNode reference
        //or null, it is equivalent to slow!==null.
        //not using it with fast, cause it is already checked above that it is not null. 
        slow = slow!.next;          // move 1 step
        fast = fast.next.next;      // move 2 steps

        if (slow === fast) {
            return true;            //cycle detected, fast will eventually come at that index again if there is a cycle
        }
    }

    return false;                   // no cycle
}
