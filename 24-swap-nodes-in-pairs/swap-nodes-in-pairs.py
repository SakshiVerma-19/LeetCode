
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        # Iterate through the list
        while current.next and current.next.next:
            # Nodes to be swapped
            first = current.next
            second = current.next.next
            
            # Swapping
            first.next = second.next
            current.next = second
            current.next.next = first
            
            current = current.next.next
        
        return dummy.next
