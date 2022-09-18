# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def list_len(listNode):
            count = 0
            while listNode:
                count +=1
                listNode = listNode.next   
            return count
            
        def swap2(listNode,k):
            dummy_list = listNode
            for num in range(int(k/2)):
                p_head = dummy_list
                p_tail = dummy_list
                for i in range(num):
                    p_head = p_head.next
                for i in range(k-num-1):
                    p_tail = p_tail.next
                
                buffer = p_head.val
                p_head.val = p_tail.val
                p_tail.val = buffer
            
        dummy_list = head
        count = list_len(dummy_list)

        for i in range(int(count/k)):
            swap2(dummy_list,k)
            for j in range(k):
                dummy_list = dummy_list.next
            
        return head