#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start

class Node:
    def __init__(self, val, index, parent):
        self.val = val
        self.index = index
        self.connections = []
        self.parent = parent
        self.connections_index = 0

    def getNextNode(self):
        if len(self.connections) == 0:
            return None

        if self.connections_index < len(self.connections):
            self.connections_index += 1
            return self.connections[self.connections_index - 1]
        else:
            return self.connections[0].getNextNode()

class Solution:
    def canJump(self, nums) -> bool:
        if len(nums) == 1 or len(nums) == 0:
            return True


        goal = len(nums) - 1
        node = Node(nums[0], 0, None)

        nodes = self.getReachableNodes(nums, node)
        node.connections = nodes

        parent_node = node
        self.addConnection(nums, node)

        root_node = node    # ONLY FOR TEST

        # TODO: Make parent_node a stack?
        # node_stack = stack(node)

        # Breadth first search
        while parent_node is not None:
            if self.addChildNodes(parent_node, nums, goal):
                return True

            # Go to next node
            parent_node = parent_node.getNextNode()

        return False

    def addChildNodes(self, parent_node, nums, goal):
        for i in range(len(parent_node.connections)):
            node = parent_node.connections[i]
            if node.index == goal:
                return True

            self.addConnection(nums, node)

        return False

    def addConnection(self, nums, node):
        for connection in node.connections:
            nodes = self.getReachableNodes(nums, connection)
            connection.connections = nodes

    def getReachableNodes(self, nums, node: Node):
        nextNodes = []
        for i in range(1, node.val+1):
            new_index = node.index + i
            if new_index < len(nums):
                nextNodes.append(Node(nums[new_index], new_index, node))

        return nextNodes
        
# @lc code=end

if __name__ == '__main__':
    s = Solution()

    # test_input = [3,0,8,2,0,0,1]
    # res = s.canJump(test_input)
    # assert res == True

    test_input = [2,3,1,1,4]
    res = s.canJump(test_input)
    assert res == True

    test_input = [3,2,1,0,4]
    res = s.canJump(test_input)
    assert res == False