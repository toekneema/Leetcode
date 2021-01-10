class Solution:
    def confusingNumber(self, N: int) -> bool:
        '''
        
        0 > rotated 180 > 0. NOT a confusing number
        
        1 > rotated 180 > 1. NOT a confusing number
        
        7 > rotated 180 > not even a valid digit after rotation.
        
        Now we can see that only a handful of digits are even VALID after rotating 180 degrees.
            - 0,1,6,8,9
        -So we can do 2 passes, the first pass we just immediately return False if one of the digits is not in that set of numbers
        -Then second pass we can reverse the string and then SWAP the digits with
            what they will transform into after rotating 180 degrees
            -and we can just hard code a map with the transformations
            {0:0}
            {1:1}
            {6:9}
            {8:8}
            {9:6}
        
        1681 > rotated 180 > 1891. IS a confusing number since 1681 != 1891
        1891
        
        
        916 > rotated 180 > 916. so it is NOT a confusing number
            
        '''
        mappings = {'0' : '0', '1' : '1', '6' : '9', '8' : '8', '9' : '6'}
        
        originalStr = str(N)
        for d in originalStr:   #first pass just filter out strings with invalid digits
            if d not in mappings:
                return False
            
        reverseStr = str(N)[::-1]  #reverse then swap with mappings
        finalStr = ''
        for c in reverseStr:
            finalStr += mappings[c]
        
        if finalStr != originalStr:
            return True
        
        return False
        
        
        