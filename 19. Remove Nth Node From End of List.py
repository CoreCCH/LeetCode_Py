# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        res = []
        len = 0
        dummy_list = head
        while dummy_list:
            len +=1
            dummy_list = dummy_list.next   

        if (len == n):
            return head.next
        #把head的起點的記憶體位置傳給dummy_list
        dummy_list = head
        for i in range(len-n-1):
            dummy_list = dummy_list.next 
        dummy_list.next = dummy_list.next.next
        return head
        