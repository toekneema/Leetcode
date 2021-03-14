class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        '''
        2 variables: stepsRemaining, xPos
        
                                                        3, 0
                                                   /      |       \
                                                 2,-1    2,0        2,1
                                                        / | \       / | \
                                                         1,0  1,1
                                                          |    
                                                         0,0
        
        
                 i 
        [x,x,x,x,x,x]
        
        stepsRemaining = 1     
        '''
        @cache
        def dfs(steps, idx):
            # pruning: not enough enough remaining steps to get back to 0
            if idx-0 > steps:
                return 0
            # out of bounds catching
            if idx >= arrLen or idx < 0:
                return 0
            if steps == 0:
                if idx == 0:
                    return 1
                return 0
            
            tmp = 0
            tmp += dfs(steps-1, idx-1)
            tmp += dfs(steps-1, idx)
            tmp += dfs(steps-1, idx+1)
            
            return tmp % MOD
            
        MOD = 10**9+7
        return dfs(steps, 0)