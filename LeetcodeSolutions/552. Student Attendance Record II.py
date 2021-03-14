class Solution:
    def checkRecord(self, n: int) -> int:
        '''
        
        
        recursively pass along:
            -n value
            -consecutive L's (only keeping track if the string ENDS in L's) (can only be 0/1/2)
            -has A or not (boolean, can only be 0/1)
        
            
            literal combinations/path tree:
            
                                 '',2,0,0
                                 
                     /             |               \
                'A',1,0,1         'L',1,1,0          'P',1,0,0
                
                 / | \           / |  \               / | \
                
               AL, AP           LA, LL, LP           PA, PL, PP
        '''
#         @cache
#         def dfs(n, consecLate, hasA):
#             if n == 0:
#                 return 1
            
#             tmp = 0
#             if not hasA:
#                 tmp += dfs(n-1, 0, True) # adding A
#                 tmp %= MOD
#             if consecLate < 2:
#                 tmp += dfs(n-1, consecLate+1, hasA)  # adding L
#                 tmp %=  MOD
#             tmp += dfs(n-1, 0, hasA) # adding P, for every case
#             tmp %= MOD 
            
#             return tmp
        
#         MOD = 10**9+7
#         return dfs(n, 0, False)
    
        #DP bottom-up now dangit
        '''
        dp[n][consecLate][hasA] stores the number of valid strings that fall under that state
                            
        6 possible states at any given string of length i:

        1: dp[i][0][0], 0 consecLate, 0 A,    PP, PLP, PLLP
        2: dp[i][0][1], 0 consecLate, 1 A, = PA, PLA, PLLA, APP, APLP, APLLP
        3: dp[i][1][0], 1 consecLate, 0 A, = dp[i-1][0][0] PPL, PP
        4: dp[i][1][1], 1 consecLate, 1 A, = dp[i-1][0][1] APPL, APP
        5: dp[i][2][0], 2 consecLate, 0 A, = dp[i-1][1][0] PPL
        6: dp[i][2][1], 2 consecLate, 1 A, = dp[i-1][1][1] APPL  


        dp[1][0][0] = 1, P
        dp[1][0][1] = 1, A
        dp[1][1][0] = 1, L
        dp[1][1][1] = 0, 
        dp[1][2][0] = 0
        dp[1][2][1] = 0
        '''
        
        MOD = 10**9+7
        dp = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(n+1)]
        dp[1][0][0] = 1
        dp[1][0][1] = 1
        dp[1][1][0] = 1
        dp[1][1][1] = 0
        dp[1][2][0] = 0
        dp[1][2][1] = 0
        for i in range(2, n+1):
            dp[i][0][0] = (dp[i-1][0][0] + dp[i-1][1][0] + dp[i-1][2][0]) % MOD #no consecLate, no A 
            dp[i][0][1] = (dp[i-1][0][0] + dp[i-1][1][0] + dp[i-1][2][0]) % MOD + (dp[i-1][0][1] + dp[i-1][1][1] + dp[i-1][2][1]) % MOD # no consecLate, has A
            dp[i][1][0] = dp[i-1][0][0] % MOD # 1 consecLate, no A
            dp[i][1][1] = dp[i-1][0][1] % MOD # 1 consecLate, has A
            dp[i][2][0] = dp[i-1][1][0] % MOD # 2 consecLate, no A
            dp[i][2][1] = dp[i-1][1][1] % MOD # 2 consecLate, has A
        
        totSum = 0
        for i in range(3):
            for j in range(2):
                totSum += dp[-1][i][j]
                totSum %= MOD
                    
        return totSum