from typing import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def LoadListNode(arr):
    head = None
    for n in arr[::-1]:
        head = ListNode(n, head)
    return head

def ListNodeToArray(node: Optional[ListNode], arr=None):
    if not arr: arr = []
    if node:
        arr.append(node.val)
        if node.next: ListNodeToArray(node.next, arr)
    return arr
