class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        '''
                  i
        nums = [2,3,1,1,1]
        maxReach = 4   #represnts an idx
        
                        i
        nums = [3,2,1,0,1]
        maxReach = 3
        
                  i
        nums = [0,2,3]
        maxReach = 0
        '''
        
        maxReach = 0
        for i in range(len(nums)):
            if maxReach >= len(nums)-1: #these 2 lines aren't necessary, but help terminate the code faster if maxReach is already >= lastIdx
                return True
            if maxReach < i:
                return False
            maxReach = max(maxReach, nums[i]+i)
        
        return True