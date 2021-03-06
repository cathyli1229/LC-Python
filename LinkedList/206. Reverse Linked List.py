class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur, prev = head, None
        while cur:
            tempNext = cur.next
            cur.next = prev
            prev = cur
            cur = tempNext
        return prev
        