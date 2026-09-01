# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        first = head
        for _ in range(n):
            first = first.next

        if first is None:
            return head.next
            
        remove = head

        while first and first.next:
            remove = remove.next
            first = first.next
        
        if remove.next:
            remove.next = remove.next.next

        return head