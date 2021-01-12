# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
    -the input is given as TreeNode obj, and the way that they represent the list version of it in the examples and stuff is thru
        a level-by-level order
        
    [2,1,3,null,null,4]
                2
                /\
              1    3
             /\    /
            N  N  4 
            
    -we're going to encode a str in a pre-order traversal order. this is the best order because it is the most basic for recursively traversing a tree
     and later when we have to build using this pre-order ordering, it is very easy
    -if you're not familiar with pre-order traversal, just know that the order of traversal processing is (root,left,right)
    
                2
                /\
              1    3
                  /
                 4   
                 
        print(currNode.val)
        traverse(currNode.left)
        traverse(currNode.right)
        
    
        deque = ''
    
                2
              /   \ 
            1       3
          /  \     / \
        N     N  4    N
                / \
              N    N
        
    
    
    
    def build():
        
        if deque[0] == 'None':
            deque.popleft()
            return None
        
        node = Node(deque[0])
        deque.popleft()
        node.left = build()
        node.right = build()    
    
        return node

'''

class Codec:

    def serialize(self, root):
        def dfs(curr):
            if not curr:
                self.serializedStr += 'None,'
                return
            self.serializedStr += str(curr.val) + ','
            dfs(curr.left)
            dfs(curr.right)            
            
        self.serializedStr = ''
        dfs(root)
        print(self.serializedStr)
        return self.serializedStr[:-1]

    def deserialize(self, data):
        """
        [5,None,None]
                        1
                        /\
                    2     3
                  /\      /\
               N    N    4  5
                        /\  /\
                      N   N N N 
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