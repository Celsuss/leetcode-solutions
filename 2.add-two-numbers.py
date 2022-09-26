#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1.val == 0:
            return l2
        elif l2.val == 0:
            return l1

        rest = 0
        root_node = ListNode()
        node = root_node

        val, rest = self.getSumAndRest(l1.val, l2.val, rest)
        node.val = val
        l1 = l1.next
        l2 = l2.next

        while l1 is not None and l2 is not None:
            l1_val = l1.val if l1 is not None else 0
            l2_val = l2.val if l2 is not None else 0

            node.next = ListNode()
            node = node.next
            val, rest = self.getSumAndRest(l1_val, l2_val, rest)
            node.val = val

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        # Add the last rest value if last sum > 10
        if rest > 0:
            node.val = rest
        if node.val == 0:
            node.next = None

        return root_node

    def getSumAndRest(self, l1_val, l2_val, rest):
        val = l1_val + l2_val + rest
        rest = val // 10
        val -= rest * 10
        return val, rest
# @lc code=end

def createLinkedList(array):
    root_node = ListNode(val=array[0])
    node = root_node
    for v in array[1:]:
        node.next = ListNode(val=v)
        node = node.next
    return root_node

def createArray(node):
    array = []
    while node.next is not None:
        array.append(node.val)
        node = node.next
    array.append(node.val)
    return array

def main():
    s = Solution()

    x1 = createLinkedList([9,9,9,9,9,9,9])
    x2 = createLinkedList([9,9,9,9])
    y = createArray(s.addTwoNumbers(x1, x2))
    assert(y == [8,9,9,9,0,0,0,1])
    x1 = createLinkedList([2,4,3])
    x2 = createLinkedList([5,6,4])
    y = createArray(s.addTwoNumbers(x1, x2))
    assert(y == [7,0,8])

    x1 = createLinkedList([0])
    x2 = createLinkedList([0])
    y = createArray(s.addTwoNumbers(x1, x2))
    assert(y == [0])


    return 0

if __name__ == '__main__':
    main()
