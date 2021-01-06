class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        #binary search variation
        #check either left or right side with mid,
        #since there's duplicates, need to have an extra condition to account for if n[mid] == n[right]
        #then just return the n[left]
        
        '''
        
        binarySearch(target=7)  #generic binary search algo
           m        
             r
         l
        [6,7,8,9,10,11]
        return -1
        
        
        
        
        
        binarySearch()           #leetcode 153, part 1
            m        
                 r
                 l
        [6,7,8,9,2,3]
        return arr[left]
        
        
        
        
        
        binarySearch()           #leetcode 154, part 2
                m        
                 r
                 l
        [8,8,8,9,2,8]
        return arr[left]
        
        
        
        
         
        binarySearch()           #another example of 154, part 2
         m        
           r
           l
        [8,2,7,8,8,8]
        return arr[left]
        
        
        
        '''
        if len(nums) == 1:
            return nums[0]
        
        left = 0
        right = len(nums) - 1
        
        if nums[left] < nums[right]: # there was no rotation
            return nums[0]
        
        while left < right:
            mid = left + (right-left) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid                
            elif nums[mid] == nums[right]:
                right -= 1
                
        return nums[left]