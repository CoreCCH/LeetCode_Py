# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def list_len(listNode):
            count = 0
            while listNode:
                count +=1
                listNode = listNode.next   
            return count
            
        def swap2(listNode):
            buffer = listNode.val
            listNode.val = listNode.next.val
            listNode.next.val = buffer
            
        dummy_list = head
        count = list_len(dummy_list)
  
        for i in range(int(count/2)):
            swap2(dummy_list)
            dummy_list = dummy_list.next.next
            
        return head