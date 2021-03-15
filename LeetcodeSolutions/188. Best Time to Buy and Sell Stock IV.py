class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        
        @cache
        def backtrack(idx, k, holding):
            if idx == len(prices) or k == 0:
                return 0
            
            # do nothing
            doNothing = backtrack(idx+1, k, holding)
            
            # make transaction
            if holding == 1: #holding something
                # sell
                doSomething = prices[idx] + backtrack(idx+1, k-1, False)
            else: # not holding anything
                # buy
                doSomething = -prices[idx] + backtrack(idx+1, k, True)
                
            return max(doNothing, doSomething)
                
        return backtrack(0, k, False)
                
                
                
        