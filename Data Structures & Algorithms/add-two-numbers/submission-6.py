# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        x = l1
        y = l2
        while x and y:
            x = x.next
            y = y.next
        if not y:
            tmp = l1
            l1 = l2
            l2 = tmp
        head = l2
        while l1:
            l2.val = l1.val + l2.val
            if l2.val >= 10:
                if l2.next:
                    l2.next.val = l2.next.val + 1
                else:
                    l2.next = ListNode(1)
                l2.val = l2.val - 10
            l1, l2 = l1.next, l2.next
        while not l1 and l2:
            if l2.val >= 10:
                if l2.next:
                    l2.next.val = l2.next.val + 1
                else:
                    l2.next = ListNode(1)
                l2.val = l2.val - 10
            l2 = l2.next
        return head


