# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False

# use slow and fast pointers; slow moves 1 step at a time while fast moves 2 steps
# if the list has a cycle, the fast pointer will eventually equal the slow pointer
# if the list doesn't have a cycle, the fast pointer will reach the end, and the loop stops
                       