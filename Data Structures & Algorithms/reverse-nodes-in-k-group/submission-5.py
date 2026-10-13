# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        temp_ls = []


        while head is not None:
            temp_ls.append(head.val)
            head = head.next

      
        new_ls = []

        for i in range(0, len(temp_ls), k):
            chunk = temp_ls[i:i+k]

            if len(chunk) == k:
                new_ls.extend(chunk[::-1])   
            else:
                new_ls.extend(chunk)         

        temp_ls = new_ls



     
        dummy = ListNode(0)
        curr = dummy

        for val in temp_ls:
            curr.next = ListNode(val)
            curr = curr.next

        return dummy.next

        