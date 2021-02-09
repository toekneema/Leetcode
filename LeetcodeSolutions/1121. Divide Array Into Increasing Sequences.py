class Solution:
    def canDivideIntoSubsequences(self, nums: List[int], K: int) -> bool:
        '''
            -pretty easy trick actually. since our constraint is pretty loose, we just need to form INCEASING SEQUENCES (not consecutive)
            -so that means each num in a sequence/partition must be unique, like 5,6,6 is invalid. but 5,6,7 is valid
            -so just make an occMap and check to see if we have enough digits in numsArray to buffer for the numOfDuplicates
            
            
            [5,6,6,7,8], K = 3
        
        
            ss1 = 6   3
            ss2 = 6   3
            
            length of 6
            
            
            6 total elements in order to satisfy the conditions
            
            
            -so really what the problem boils down to is how many occurrences of each number are there. we just need to make
                sure we have enough elements
            
            
            
            [1,2,2,3,3,4,4], K = 3, n = 7
            occ = {1:1}
                  {2:2}
                  {3:2}
                  {4:2}
            
            
            
            [1,2,2,2,3], k=3
            
            ss1 = 2  3
            ss2 = 2  3
            ss3 = 2  3
            
            9
            
        '''
        
        n = len(nums)
        occ = defaultdict(int)
        for num in nums:
            occ[num] += 1
            if occ[num] * K > n:
                return False
            
        return True