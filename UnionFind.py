class UnionFind:
    '''           
    graph = [[1,1,0],[1,1,0],[0,0,1]], initial = [0,1]
            
            0>1>3>4
            v
            2
            
    parents = [0,0,0,0,0]
    size =    [5,1,1,1,1]   #oh yeaaaaaa, the sizes will ONLY be correct for the TOP parents themselves, nothing else matters
     
    '''
    def __init__(self, length):
        self.parents = [0] * length
        for i in range(length):
            self.parents[i] = i
        self.sizes = [1] * length
        
        self.numOfComponents = length
    
    def find(self, target): #find the top parent of "target" 
        '''
        target = node id 1
        '''
        parent = target
        while parent != self.parents[parent]:  #at the end of this, it will find the og/top parent and that value will be stored in 'parent'
            parent = self.parents[parent]
        
        #this next part is the compression along the way, so if the parents were all linear like this: 0>1>3>4, then the graph becomes
            #           1
            #           ^
            #       4 < 0 > 3  this way it is amortizing the time to find the parent node for the future
        
        while target != parent:
            nextTarget = self.parents[target]
            self.parents[target] = parent
            target = nextTarget
            
    
        return parent
        
        
    def union(self, target1, target2):  #merge the component that "target1" belongs to and the component that "target2" belongs to
        parent1 = self.find(target1)
        parent2 = self.find(target2)
        
        if parent1 != parent2:
            if self.sizes[parent1] >= self.sizes[parent2]:
                #merge parent2 into parent2
                self.sizes[parent1] += self.sizes[parent2]
                self.parents[parent2] = parent1
            else:
                #merge parent 1 into parent2
                self.sizes[parent2] += self.sizes[parent1]
                self.parents[parent1] = parent2
                
            self.numOfComponents -= 1
            
            
    def componentSize(self, target): #find the size of the component that "target" belongs to
        return self.sizes[find(target)]
    
    def connected(self, target1, target2): #returns boolean whether the two components target1/target2 belong to are the same or not
        return self.find(target1) == self.find(target2)