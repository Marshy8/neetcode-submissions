# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy = head

        while dummy and dummy.next:
            head = head.next
            dummy = dummy.next.next
            if head == dummy:
                return True
            
        return False