Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        que,depth = deque([root]),1
        while que:
            for i in range(len(que)):
                node = que.popleft()
                if not node: continue
                elif not (node.left or node.right):
                    return depth
                else:
                    que.append(node.left)
                    que.append(node.right)
            depth += 1
        return depth
