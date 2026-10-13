# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
            if not head:
                return

            a = []
            curr = head

            # Step 1: store values
            while curr:
                a.append(curr.val)
                curr = curr.next

            # Step 2: reorder array
            new_ls = []
            i, j = 0, len(a) - 1
            while i <= j:
                new_ls.append(a[i])
                i += 1
                if i <= j:
                    new_ls.append(a[j])
                    j -= 1

            # Step 3: write back to linked list
            curr = head
            idx = 0
            while curr:
                curr.val = new_ls[idx]
                idx += 1
                curr = curr.next
        
        
        