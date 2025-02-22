# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        stack = []
        i = 0
        
        while i < len(traversal):
            level = 0
            while i < len(traversal) and traversal[i] == '-':
                level += 1
                i += 1
            
            value = 0
            while i < len(traversal) and traversal[i].isdigit():
                value = value * 10 + int(traversal[i])
                i += 1
            
            node = TreeNode(value)
            
            if level == len(stack):
                if stack:
                    stack[-1].left = node
            else:
                while level != len(stack):
                    stack.pop()
                stack[-1].right = node
            
            stack.append(node)
        
        while len(stack) > 1:
            stack.pop()
        return stack[0]

    def bfs(self, root: TreeNode):
        if not root:
            return []
        
        queue = deque([root])
        result = []
        
        while queue:
            node = queue.popleft()
            result.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return result