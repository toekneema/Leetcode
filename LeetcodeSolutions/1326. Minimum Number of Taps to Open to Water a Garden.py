class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        '''
        -first create the intervals
        -then do the leetcode 1024 stitching video algo
            -this is essentially just creating a list of bestReaches for each startingIdx
        -then doing jump game ii algo on that new list
            -basically like a BFS layer-by-layer traversal on a 1 dimensional array
            
                            n
                  0 1 2 3 4 5 
        ranges = [3,4,1,1,0,0]
        [0,3]
        [0,5]
        [1,3]
        [2,4]
        [4,4]
        [5,5]
           
                                               n=100001
                       0 1 2 3 4 5 6 7 8 9
        bestReaches = [5,3,4,x,4,5, , , , , , , , ]  []*10001
            
            
        
        
        JUMP GAME II
        
                 i
         0 1 2 3 4
        [3,2,1,0,1]
        
         0     1     2
        (3) (2,1,0) (1)
        
        maxReach = 3 
        jumps = 2
        layerEnd = 3
            
            
        '''
        intervals = []
        for i,num in enumerate(ranges):
            left = max(0, i-num)
            right = min(len(ranges), i+num)
            intervals.append([left,right])
        print(intervals)
        
        bestReaches = [0] * 10001
        for left,right in intervals:
            bestReaches[left] = max(bestReaches[left], right)
            
        #print(bestReaches)
        
        maxReach = 0
        layerEnd = 0
        jumps = 0
        for i in range(n+1):
            if i > maxReach:
                return -1
            
            if layerEnd >= n:
                return jumps
            
            maxReach = max(maxReach, bestReaches[i])
            
            if i == layerEnd:
                jumps += 1
                layerEnd = maxReach
                
        