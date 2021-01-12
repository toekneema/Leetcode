# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        def dfs(curr):
            if not curr:
                self.serializedStr += 'None,'
                return
            self.serializedStr += str(curr.val) + ','
            dfs(curr.left)
            dfs(curr.right)
            
        self.serializedStr = ''
        dfs(root)
        return self.serializedStr[:-1]
        

    def deserialize(self, data: str) -> TreeNode:
        """
        use pre-order DFS traversal recursion to build tree again
                2
                /\
            1      3 
            /\     /\
       None   NoneNone None
       
       trick here is to use a deque and just always take the first element and then just pop it off
        """
        def dfs():
            if not d:
                return None
            if d[0] == 'None':
                d.popleft()
                return None
            
            node = TreeNode(int(d[0]))
            d.popleft()
            node.left = dfs()
            node.right = dfs()
            
            return node
            
        d = deque(data.split(','))
        return dfs()