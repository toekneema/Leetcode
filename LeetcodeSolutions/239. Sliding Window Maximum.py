class Solution:
    def maxSlidingWindow(self, nums, k):
        '''
        -the deque will hold the MAX value of the current window at the FRONT (d[0])
        -remove anything that is less than/equal to i-k   #removes anything that isnt in your currWindowRange
        -then you can try to insert the currNum into the back of the deque, but first you need to remove all elements LESS than it before inserting
        -once i+1 - k >= 0: start appending the front of deque into outputArr
        
                         i
         0 1  2  3 4 5 6 7
        [1,3,-1,-3,5,3,6,7], k = 3
        
        
        d = [7]      #the deque should be in dec order
        output = [3,3,5,5,6,7]
        
        
        
                      i
          0  1  2 3 4 5
        [10,-5,-2,4,0,3], k = 3
        
        d = [4,3]     #dec order is maintained
        output = [10,4,4,4]
        
        
        '''
        
        d = deque()
        output = []
        
        for i in range(len(nums)):
            while d and nums[d[-1]] < nums[i]:
                d.pop()
            d.append(i)
            if i-k == d[0]:
                d.popleft()
            if i+1 - k >= 0:
                output.append(nums[d[0]])
            
        return output