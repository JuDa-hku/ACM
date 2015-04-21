# Definition for a  binary tree node
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def rightSideView(self, root):
        result = []
        if root == None:
            return result
        nodesList = [[root]]
        while len(nodesList)!=0:
            nodes = nodesList.pop(0)
            result.append(nodes[-1].val)
            nodeSonList = []
            for node in nodes:
                if node.left != None:
                    nodeSonList.append(node.left)
                if node.right != None:
                    nodeSonList.append(node.right)
            if nodeSonList != []:
                nodesList.append(nodeSonList)
        return result
                    
            
            
            
        

root = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node2.right = node5
node3.right = node4
root.left = node2
root.right = node3

s = Solution()

root1 = TreeNode(1)
node2 = TreeNode(2)
root1.left = node2
print s.rightSideView(root)
print s.rightSideView(root1)