class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        '''  0 1 2 3 4
         0   @ . a . #
         1   # # # . # 
         2   b . A . B 
            
            keyCount = 2
            visited = ((0,0,''),(0,1,''),(0,2,''),(0,3,'a')     )
            q = []
            
            
            0 1 2 3 4
        0   @ . . . a
        1   . # # # A
        2   b . B C c 
        
            keyCount = 3
            visited = ((0,0,''),(1,0,''),(0,1,''),   )
            q = []
            
            0 1 2 3 4
        0   D d # b @
        1   . f E . e
        2   # # . B .
        3   # . c A .         #WOWWWWW, the bug was that it was doing nothing when i passed the 'f' again on the way back
        4   a F . # C             #i need to add all directions again in that case. WOW
            
            visited = ((1,3,'b'),(1,3,'be'))
            q = [(0,1,'ebf')]
            
            
            -im going to want to do a BFS, and each time store the key string, as well as put that into a visited set
            -yep so first pass i will just find the start point and then find keyCount
                
        '''
        
        n = len(grid)
        m = len(grid[0])
        keySet = set(['a','b','c','d','e','f'])
        lockSet = set(['A','B','C','D','E','F'])
        
        
        keyCount = 0
        start = (0,0,'')  # (i,j,keyStr)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '@':
                    start = (i,j,'')
                elif grid[i][j] in keySet:
                    keyCount += 1
        
        q = deque()
        q.append(start)
        q2 = deque()
        visited = set()
        #visited2 = set()
        directions = [[0,-1],[0,1],[-1,0],[1,0]]
        
        def addAllDirections(i,j,keyStr):
            for d in directions:
                r = i+d[0]
                c = j+d[1]
                    
                
                if r<0 or c<0 or r>=n or c>=m:
                    continue
                q.append((r,c,keyStr))
                
        steps = 0
        
        while q:
            level = []
            while q:
                level.append(q.popleft())
                
            for state in level:
                i,j,keyStr = state
                
                if (i,j,keyStr) in visited or grid[i][j] == '#':
                    continue
                
                c = grid[i][j]
                if c in lockSet:
                    if c.lower() not in keyStr:
                        continue
                    else: #so i DID have the key to this lock. THIS LINE HERE MIGHT BE FUCKKKKED
                        addAllDirections(i,j,keyStr)
                elif c in keySet:
                    if c not in keyStr:
                        keyStr += c
                        if len(keyStr) == keyCount:
                            return steps
                        addAllDirections(i,j,keyStr)
                    else:
                        addAllDirections(i,j,keyStr)
                else:
                    addAllDirections(i,j,keyStr)
            
                visited.add((i,j,keyStr))
                #if i==2 and j==2:
                    #visited2.add((i,j,keyStr))
                    
            steps += 1    
        
        return -1
                
        