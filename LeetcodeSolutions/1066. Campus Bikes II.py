class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        '''
        start at worker 0, go til last worker
            -for each worker, ill iterate thru all the bikes
                -if its not been visited yet, then mark as used and update dists
                
        '''
        
        def findDist(x,y):
            return abs(x[0]- y[0]) + abs(x[1] - y[1])
        
        @cache
        def dfs(workerIdx, mask):
            if workerIdx == len(workers):
                return 0
            
            tmp = float('inf')
            for i in range(len(bikes)):
                if mask & 1<<i:
                    continue
                dist = findDist(workers[workerIdx], bikes[i])
                dist += dfs(workerIdx+1, mask | 1<<i)
                tmp = min(tmp, dist)
            
            return tmp
        
        return dfs(0, 0)