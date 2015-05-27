# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        seen = {}
        return self.cloneGraphHelp(node, seen)


    def cloneGraphHelp(self, node, seen):
        if not node:
            return None
        if node in seen:
            return seen[node]
        newNode = UndirectedGraphNode(node.label)
        seen[node] = newNode
        for n in node.neighbors:
            newNode.neighbors.append(self.cloneGraphHelp(n, seen))
        return newNode