# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        anchor = head
        chain = head

        while chain != None and chain.next != None:
            chain = chain.next.next
            anchor = anchor.next
            if chain == anchor:
                return True
        return False
        