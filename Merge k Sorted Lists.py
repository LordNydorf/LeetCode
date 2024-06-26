# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        d=defaultdict(int)
        for i in lists:
            head=ListNode(0)
            head.next=i
            head=head.next
            while head:
                d[head.val]+=1
                head=head.next
        head=ListNode(0)
        cur=head
        val=sorted(d.keys(), reverse=True)
        while val:
            k=val.pop()
            for i in range(d[k]):
                cur.next=ListNode(k)
                cur=cur.next
        return head.next
