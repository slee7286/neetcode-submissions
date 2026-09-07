class Solution:
    def nextK(self, node: Optional[ListNode], k: int):
        while node and k > 1:
            node = node.next
            k -= 1

        return node

    def reverseKGroup(
        self,
        head: Optional[ListNode],
        k: int
    ) -> Optional[ListNode]:

        dummy = ListNode(0, head)

        group_prev = dummy

        while True:
            # Find kth node of current group
            kth = self.nextK(group_prev.next, k)

            # Fewer than k nodes remain
            if kth is None:
                break

            # Save node after group
            group_next = kth.next

            # Reverse the group
            prev = group_next
            curr = group_prev.next

            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # Old first node is now the last node
            old_group_start = group_prev.next

            # kth is now the first node
            group_prev.next = kth

            # Move group_prev to end of reversed group
            group_prev = old_group_start

        return dummy.next