"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

'''
no diff than the other two serialize/deserialize Binary tree problems (297/449). just instead of doing left and right child , just loop thru all children lol
still use a preorder DFS recursive approach for both s/d
-ahhh i see the issue now. its that i dont know how many children it should have, and the for loop will never run on a null child
    so im never adding those null markers so help me deserialize later. so its going to be impossible to know how to partition the deserialize
    -ahhhhhhh so i can just add another piece of data, which is the numOfChildren for each node. that will help me build it later on
    
    
    
    -instead of recursively calling dfs(left) and dfs(right)
    - N-ary trees you have to loop thru all children
    
            for child in children:
                dfs(child)
                
    serializedStr = 1,3,5,None,None,6,None,None,2,None,None,4,None,None       
    pre-order traversal is just (root, left, right)
    
             
        
    
    1#3,3#2,5#0,6#0,2#0,4#0         each section represents the node and numOfChildren
    
    -use pre-order traversal to generate this serializedStr ()
    
    
    
    now that we have the serializedStr, lets see how to re-create the tree from this string
    
    d = []
    
                       1#3
                     /  |   \
                3#2    2#0   4#0
                /   \   
            5#0     6#0     
             
            
    recursive call stack = []
    
    def dfs():
        val, numOfChildren = d.popleft()
        node = Node(val)
        for i in range(numOfChildren):
            node.children.append(dfs())
            
        return node
    
'''

class Codec:
    def serialize(self, root: 'Node') -> str:
        def dfs(curr):
            if not curr:
                self.serializeStr += 'None,'
                return
            self.serializeStr += str(curr.val) + '#'
            self.serializeStr += str(len(curr.children)) + ','
            for c in curr.children:
                dfs(c)
        
        if not root:
            return ''
        self.serializeStr = ''
        dfs(root)
        return self.serializeStr[:-1]
        
    def deserialize(self, data: str) -> 'Node':
        def dfs():
            if not d:
                return None
            
            dataCombo = d.popleft()
            val,numOfChilds = dataCombo.split('#')
            
            node = Node(int(val))
            node.children = []
            for i in range(int(numOfChilds)):
                node.children.append(dfs())
            
            return node
        
        if not data:
            return None
        d = deque(data.split(','))
        return dfs()
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))