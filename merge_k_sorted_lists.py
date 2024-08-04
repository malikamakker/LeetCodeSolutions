# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def add_new_node(self, lists, new_node):
        if not new_node:
            return
        start = 0
        end = len(lists) - 1
        while start <= end:
            mid = (start + end) // 2
            if lists[mid].val <= new_node.val:
                start = mid + 1
            elif lists[mid].val > new_node.val:
                end = mid - 1
        lists.insert(start, new_node)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lists = [_list for _list in lists if _list]
        lists.sort(key=lambda x:x.val)
        root = None
        current = None
        prev = None

        while lists:
            first_node = lists.pop(0)
            current = ListNode(first_node.val)
            if prev:
                prev.next = current
            else:
                root = current
            prev = current
            self.add_new_node(lists, first_node.next)
        
        return root
        