class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next      # 1. save the rest of the list
            curr.next = prev     # 2. flip the pointer
            prev = curr          # 3. advance prev
            curr = nxt           # 4. advance curr

        return prev              # prev is the new head