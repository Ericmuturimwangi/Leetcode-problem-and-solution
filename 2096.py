class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        self.startNode = None
        self.endNode = None

        def dfs(root, parent):
            if not root:
                return