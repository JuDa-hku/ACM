# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

        
class Solution:
    # @param {TreeNode} root
    # @return {integer}

    def maxPathSum(self, root):
        if not root.right and not root.left:
            return root.val
        res = [0]
        self.maxPathSumHelp(root, res)
        if res[0] == 0:
            return self.minimumValue(root)
        return res[0]
        

    def minimumValue(self, root):
        mini = root.val
        stack = [root]
        while stack:
            root = stack.pop()
            if root.right:
                stack.append(root.right)
            if root.left:
                stack.append(root.left)
            mini = max(mini, root.val)
        return mini
        
    def maxPathSumHelp(self, root, res):
        if not root:
            return 0
        r = max(self.maxPathSumHelp(root.right, res), 0)
        l = max(self.maxPathSumHelp(root.left, res),0)
        res[0] = max(res[0], r+l+root.val)
        return max(r,l) + root.val


s = Solution()
a1,a2,a3 = TreeNode(-1),TreeNode(-2),TreeNode(-3)
a1.right, a1.left = a2, a3
a2.left, a2.right = TreeNode(-100), TreeNode(-10)
print s.maxPathSum(a1)