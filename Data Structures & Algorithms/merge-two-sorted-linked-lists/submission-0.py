# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        left, right = list1, list2

        if left.val >= right.val:
            head = right
        else:
            head = left

        while left and right:
            if left.val >= right.val:
                left, right = right, left
            node_next = left.next
            if node_next is None or node_next.val >= right.val:
                left.next = right
            left = node_next
            
        return head
            

        
