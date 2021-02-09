class Solution:
    def stoneGameIII(self, sV: List[int]) -> str:
        '''
            idea here is to explore all possible combos, so i need to use reucrsion/dp instead of greedy
            
            at each recursive statement, i can try 3 different options.
            -taking just 1 stone, taking 2 stones, taking all 3 stones
                -so i need to choose the max of these 3 options
                
                
                
            -with any sort of DP problem, there is a base case/subproblem. so lets look at these
            -when there is only 1 stone, the best score is just that stone
            -when there is 2 stones, the best score is either take both stones or stone1-stone2
            -when there are 3 or more stones, alice's score is the max of three options: the ans from taking 1 stone, the ans from taking 2 stones,
                or taking 3 stones
            
            
            -lets define what EACH DP index means
                -dp[i] stores the BEST difference (aliceScore - bobScore) if the list of stones started at idx i
            
            6,7
            5 - f(6,7)
            5+6 - f(7)
            5+6+7 - f()
            
                        1
            values = [1,2,3,7]
                        /\
            1 - f(2,3,7),  1+2 - f(3,7),   1+2+3 - f(7)
                /\                                  /\
    2 - f(3,7), 2+3 - f(7), 2+3+7 - f()           7 - f()
    
    
    
            [1,2,3,7]
                /\
        1-12, 3-10, 6-7
        -11,  -7,   -1
        
        
        
        [5,6,7]
        alice has 5, bob has 13, diff is -8
        alice has 11, bob has 7, diff 4
        alice has 18, bob has 0, diff is 18
        
        
                     0 1 2
        stoneList = [5,6,7]
            dp    = [18,13,7]
            if dp[0] 
            
            
            
            
            
            
        
        
        '''
        
        
        
        
        
        
        
        
        
        
        
        
        #top-down recursive DFS + memo
        
        def recurse(i):
            if i >= len(sV):
                return 0
            
            if i in cache:
                return cache[i]
            
            best = float('-inf')
            if i == len(sV) - 1:   #this means the array is length 1
                best = sV[i] #take1, well i mean you only have 1 option anyways lol
            elif i == len(sV) - 2: #this means the array is length 2
                # take1 = sV[i] - recurse(i+1)
                # take2 = sV[i]+sV[i+1] - recurse(i+2)
                take1 = sV[i] - sV[i+1]
                take2 = sV[i]+sV[i+1]
                best = max(take1,take2)
            else: #now this main part is when the len is 3 or more, so i must try all 3 cases
                take1 = sV[i] - recurse(i+1)
                take2 = sV[i]+sV[i+1] - recurse(i+2)
                take3 = sV[i]+sV[i+1]+sV[i+2] - recurse(i+3)
                best = max(take1,take2,take3)
            
            cache[i] = best
            return cache[i]
        
        cache = {}
        aliceBestDiff = recurse(0)
        if aliceBestDiff > 0: return 'Alice'
        if aliceBestDiff < 0: return 'Bob'
        return 'Tie'
            
    
    
    
    
    
    
    
    
    
    
    
        #bottom-up iterative DP
        
        dp = [0] * (len(sV)+1)
        for i in range(len(sV)-1,-1,-1):
            best = float('-inf')
            if i == len(sV)-1:
                best = sV[i]  #take1
            elif i == len(sV)-2:
                take1 = sV[i] - sV[i+1]
                take2 = sV[i]+sV[i+1]
                best = max(take1,take2)
            else: #subproblem is 3 or more stones long
                take1 = sV[i] - dp[i+1]
                take2 = sV[i]+sV[i+1] - dp[i+2]
                take3 = sV[i]+sV[i+1]+sV[i+2] - dp[i+3]
                best = max(take1,take2,take3)
            
            dp[i] = best
        
        if dp[0] > 0: return 'Alice'
        if dp[0] < 0: return 'Bob'
        return 'Tie'