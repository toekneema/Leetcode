class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        '''
        
        
          1  2 3 4  5
        [-1,-8,0,5,-9]
        1*-1 + 2*-8 + 3*0 + 4*5 + 5*-9 = -42
        
        
        now we should realize that we need to sort so that the higher satisfactions line up with the latter times
        
          1 2 3 4  5
        [ 0,5]
        1*-1 + 2*0 + 3*5 = 14             
        
        
        but then comes the question, when do we need to remove dishes and how do we determine how many to delete
        -we could brute force one by one starting from the left and then recalculate each time*satisfactions again O(N^2)
        -or we can use a clever trick by understanding that each time we remove the leftmost item
            we will shift each value over by 1 time unit and thus the totalSatisfaction will decrease at each idx by that amount 
            -so instead of the satisfaction of 4 being at time 3, it is at time 2, so that change of 1 time unit decreases the
                totalSatisfaction by 4, same thing happens with the 3. the satisfaction of 3 used to be at time 2, but now its at time 1
                so the totalSatisfaction decreased by 3
                -so what we're really doing here is just taking the sumTotal of the whole array and subtracting that from
                    totalSatisfaction
        
        -then once we realize that each time we remove the leftmost dish that its just doing productTotal-sumTotal, then we can just keep
            removing the leftmost dish while our sumTotal is negative bc productTotal - (-x) is actually increasing our
            productTotal. but once sumTotal becomes positive then it is actually going to decrease our productTotal so we need to stop iterating
        
         1 2
        [3,4]
        sumTotal = 9
        productTotal = 1*2 + 2*3 + 3*4 = 20
         1 2
        [3,4]
        sumTotal = 7
        productTotal = 1*3 + 2*4 = 11
         1
        [4]
        productTotal = 1*4 = 4
        
        
        
          1  2  3 4 5
        [-9,-8,-1,0,5]
        sumTotal = -13
        productTotal = -9 -16 -3 + 25 = -3 - (-13)
        [-8,-1,0,5]
        sumTotal = -4
        productTotal = -8 -2 + 20 = 10-(-4)
        [-1,0,5]
        sumTotal = 4
        productTotal = -1 + 15 = 14
        [0,5]
        sumTotal = 5
        productTotal = 10
        
        
        
          1  2  3 4 5 6
        [-3,-2,-1,0,3,5]
        sumTotal = 2
        productTotal = -3 -4 -3 + 15 + 30    = 35 
        [-2,-1,0,3,5]
        sumTotal = 5
        productTotal = -2 -2 + 12 + 25 = 33
        [-1,0,3,5]
        sumTotal = 7
        productTotal = -1 + 9 + 20 = 28
        [0,3,5]
        productTotal = 6 + 15 = 21
                              
        
        
        '''
        
        satisfaction.sort()
        satisfaction = deque(satisfaction) #easier to popleft now
        
        sumTotal = sum(satisfaction)
        productTotal = 0
        
        for i,num in enumerate(satisfaction):
            productTotal += num*(i+1)
            
        while sumTotal < 0:
            productTotal -= sumTotal
            sumTotal -= satisfaction.popleft()
            
            
        return max(0, productTotal)