# transform a vector to tree structure and # means the dead end
class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

def vectorToTree(vector):
    result = TreeNode(vector.pop(0))
    stack = [result]
    while vector :
        root = stack.pop(0)
        if root.value != '#':
            valueLeft = vector.pop(0)
            if valueLeft != '#':
                root.left = TreeNode(valueLeft)
                stack.append(root.left)
            valueRight = vector.pop(0)
            if valueRight != '#':
                root.right = TreeNode(valueRight)
                stack.append(root.left)
    return result

res = vectorToTree([1,2,'#',3,4,5,6])

    