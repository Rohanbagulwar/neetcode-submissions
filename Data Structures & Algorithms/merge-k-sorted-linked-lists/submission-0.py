
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return 
        if len(lists)==1:
            return lists[0]

        final_node=lists[0]
        
        for i in range(1,len(lists)):
            final_node=self.mergetwo(final_node,lists[i])

        return final_node


    
    def mergetwo(self,first, second):
        temp_ls = []
    
        # take values from first list
        while first is not None:
            temp_ls.append(first.val)
            first = first.next
    
        # take values from second list
        while second is not None:
            temp_ls.append(second.val)
            second = second.next
    
        # sort values
        temp_ls.sort()
    
        # insert all values into a new linked list (at last node)
        dummy = ListNode(0)
        curr = dummy
    
        for val in temp_ls:
            curr.next = ListNode(val)
            curr = curr.next
    
        return dummy.next
    
        

        
        
                
        
        