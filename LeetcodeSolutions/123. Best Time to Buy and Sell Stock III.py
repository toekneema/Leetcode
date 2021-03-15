class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        
         
         i
        [7,6,4,3,1]
        
                                            0, 2, False
                                        /               \
                                    1,2,False         1,2,True
                                    /    \               /    \
                                 2,2,F   2,2,T       2,2,T    2,1,F
                                                        
        i
        transactionsLeft = 2
        holding = False
        
        '''
        @cache
        def backtrack(idx, k, holding):
            if idx == len(prices) or k==0:
                return 0
            
            #doing nothing
            doNothing = backtrack(idx+1, k, holding)
            
            #doing something
            if holding: #sell
                doSomething = prices[idx] + backtrack(idx+1, k-1, False)
            else: #buy
                doSomething = -prices[idx] + backtrack(idx+1, k, True)
            
            return max(doNothing, doSomething)
        
        return backtrack(0, 2, False)