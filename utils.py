
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def createLinkedListFromArray(array):
    root_node = ListNode(val=array[0])
    node = root_node
    for v in array[1:]:
        node.next = ListNode(val=v)
        node = node.next
    return root_node

def createArrayFromLinkedList(node):
    array = []
    if node is None:
        return array

    while node.next is not None:
        array.append(node.val)
        node = node.next
    array.append(node.val)
    return array