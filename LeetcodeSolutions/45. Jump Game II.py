class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
         i
        [3,3,1,1,2,1,1]          O(N^2) approach
        reachRange = (1,4)
        maxReach = 4
        jumps = 1
        
        
        
               i
        [3,3,1,1,4]          O(N) approach
        maxReach = 4
        jumps = 2
        rangeEnd = 4
        
        
                 i
        [1,3,1,2,0,1]
        maxReach = 5
        jumps = 3
        rangeEnd = 5
        
        
        '''
        
        jumps, rangeEnd, maxReach = 0, 0, 0
        for i in range(len(nums)):
            if rangeEnd >= len(nums)-1:  #meaning it reached the last idx in the list
                return jumps
            maxReach = max(maxReach, nums[i] + i)
            if i == rangeEnd:
                rangeEnd = maxReach
                jumps += 1
            
        return jumps