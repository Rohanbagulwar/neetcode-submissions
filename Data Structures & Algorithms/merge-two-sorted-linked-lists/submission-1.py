# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ls1=[]

        if list1 is not None:
            head=list1
            while head is not None:
                ls1.append(head.val)
                head=head.next
        if list2 is not None:
            head=list2
            while head is not None:
                ls1.append(head.val)
                head=head.next
        
        ls1.sort()

        dummy=ListNode(0)
        curr=dummy

        for i in ls1:
            curr.next=ListNode(i)
            curr=curr.next
        return dummy.next
            

        