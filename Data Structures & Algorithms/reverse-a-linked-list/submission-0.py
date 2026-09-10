# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev            

# solve using two pointers, since we're only reversing
# initialize the current pointer to the head node, and a previous pointer to null
# each iteration, set curr.next to prev pointer, and then shift pointers     