# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def helper(pre_start, pre_end, post_start, post_end):
            if pre_start > pre_end:
                return None

            root = TreeNode(preorder[pre_start])
            if pre_start == pre_end:
                return root

            left_root_val = preorder[pre_start + 1]
            left_root_idx = postorder.index(left_root_val)

            left_subtree_size = left_root_idx - post_start + 1

            root.left = helper(pre_start + 1, pre_start + left_subtree_size, post_start, left_root_idx)
            root.right = helper(pre_start + left_subtree_size + 1, pre_end, left_root_idx + 1, post_end - 1)

            return root

        return helper(0, len(preorder) - 1, 0, len(postorder) - 1)
            