#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

import utils

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        root = ListNode(0, head)
        prev_node = root
        while prev_node.next is not None and prev_node.next.next is not None:
            node = prev_node.next
            next_node = prev_node.next.next
            third_node = prev_node.next.next.next if next_node is not None else None

            prev_node.next = next_node
            prev_node.next.next = node
            prev_node.next.next.next = third_node

            prev_node = prev_node.next.next
            continue

        return root.next
        
# @lc code=end

def main():
    s = Solution()

    x = [1, 2, 3]
    x = utils.createLinkedListFromArray(x)
    y = s.swapPairs(x)
    y = utils.createArrayFromLinkedList(y)
    assert(y == [2,1,3])

    x = [1, 2, 3, 4]
    x = utils.createLinkedListFromArray(x)
    y = s.swapPairs(x)
    y = utils.createArrayFromLinkedList(y)
    assert(y == [2,1,4,3])

    return 0

if __name__ == '__main__':
    main()