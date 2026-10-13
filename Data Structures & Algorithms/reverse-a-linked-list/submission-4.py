# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a=[]
        while head is not None:
            a.append(head.val)
            head=head.next
        a=a[::-1]
        
        dummy=ListNode(0)
        curr=dummy
        for i in a:
            curr.next=ListNode(i)
            curr=curr.next
        return dummy.next