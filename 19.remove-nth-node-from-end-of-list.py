#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

import utils

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head.next is None:
            return None

        left_node = head
        right_node = self.getRightNode(left_node, n)

        if right_node is None:
            return left_node.next

        while right_node.next is not None:
            left_node = left_node.next
            right_node = right_node.next

        left_node.next = left_node.next.next

        return head
    
    def getRightNode(self, left_node: ListNode, n: int) -> ListNode:
        right_node = left_node
        for i in range(n):
            right_node = right_node.next

        return right_node

# @lc code=end

def main():
    s = Solution()

    x = [1,2,3,4,5,6,7,8,9,10]
    n = 7
    x = utils.createLinkedListFromArray(x)
    y = s.removeNthFromEnd(x, n)
    y = utils.createArrayFromLinkedList(y)
    assert(y == [1,2,3,5,6,7,8,9,10])

    x = [1, 2, 3, 4, 5]
    n = 2
    x = utils.createLinkedListFromArray(x)
    y = s.removeNthFromEnd(x, n)
    y = utils.createArrayFromLinkedList(y)
    assert(y == [1,2,3,5])

    x = [1]
    n = 1
    x = utils.createLinkedListFromArray(x)
    y = s.removeNthFromEnd(x, n)
    y = utils.createArrayFromLinkedList(y)
    assert(y == [])

    x = [1, 2]
    n = 1
    x = utils.createLinkedListFromArray(x)
    y = s.removeNthFromEnd(x, n)
    y = utils.createArrayFromLinkedList(y)
    assert(y == [1])

    x = [1, 2]
    n = 2
    x = utils.createLinkedListFromArray(x)
    y = s.removeNthFromEnd(x, n)
    y = utils.createArrayFromLinkedList(y)
    assert(y == [2])

    return 0

if __name__ == '__main__':
    main()