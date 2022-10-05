

#############
# Tree Node #
#############
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createTreeFromArray(array):
    if array is None or len(array) == 0:
        return None
        
    def createNode(i):
        if i >= len(array):
            return None

        node = TreeNode(array[i])
        node.left = createNode(i * 2 + 1)
        node.right = createNode(i * 2 + 2)

        return node
    
    return createNode(0)

def createArrayFromTree(root: TreeNode):
    if root is None or root.val is None:
        return []

    res = []
    queue = [root]
    def breadthFirst(node: TreeNode):
        if node is None:
            return
        res.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
        queue.pop(0)
        breadthFirst(queue[0])
    breadthFirst(root)
    return res

#############
# List Node #
#############
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

def createArrayFromLinkedList(node: ListNode):
    array = []
    if node is None:
        return array

    while node.next is not None:
        array.append(node.val)
        node = node.next
    array.append(node.val)
    return array