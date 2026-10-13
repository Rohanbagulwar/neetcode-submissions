# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        a = []
        new_ls = []
        count = 0
        new_count = 0
        full_count = 0

        curr = head   # save head

        # store values
        while curr:
            a.append(curr.val)   # FIX: ls -> a
            curr = curr.next

        # reorder array
        while len(new_ls) != len(a):
            if full_count % 2 == 0:
                new_ls.append(a[count])
                count += 1
            else:
                new_count += 1
                new_ls.append(a[len(a) - new_count])
            full_count += 1

        # write back to linked list
        curr = head
        i = 0
        while curr:
            curr.val = new_ls[i]
            i += 1            # FIX: missing increment
            curr = curr.next