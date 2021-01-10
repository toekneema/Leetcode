class Solution:
    def confusingNumberII(self, N: int) -> int:
        
        '''
            -how do i create these combos/permutations.
            -okay so the key here is to add these numbers to the RIGHT of the currNum
            -to do that, i need to multiply the currNum by 10, then add that number
                -lets say im at 89 and i want to create the next 5 combos.
                -89*10 = 890, then 890+0... 890+1.... 890+6... 890+8.... 890+9
            
            
            -start from 1. dont need to add to the right side of 0 because those combos like 0100, 0109 will already be covered by the other recursive calls
            0       1           6           8           9
                    /\          /\         /\          /\
           n/a    10...19    60...69     80...89     90...99
                  /\                          /\
              100....109                   890...899
     
              
        
        
        Time Complexity Analysis:
        
        
        0-100:  (process about 25 numbers, so 100/25 is already about n/4)
        
        1,6,8,9
        10,11,16,18,19
        60,61,66,68,69
        80,81,86,88,89
        90,91,96,98,99
        
        100-1000:    (process about 100 numbers, so 1000/100 is already n/10)
        
        100, 101, 106, 108, 109
        110, 111, 116, 118, 119
        160, 161, 166, 168, 169
        180, 181, 186, 188, 189
        190, 191, 196, 198, 199
        
        6 - another 25
        
        8 - another 25
        
        9 - another 25
        
        
        
        continue applying the same logic for 1000-10000: (process about 400 numbers, so 10000/400 is already n/25)
        
        1000s - about 100 numbers
        
        6000s - about 100 numbers
        
        8000s - about 100 numbers
        
        9000s - about 100 numbers
        
        
        Time Complexity = O(logN)
        
        '''
        
        mappings = {'0' : '0', '1' : '1', '6' : '9', '8' : '8', '9' : '6'}
        
        
        def isConfusingNumber(s):         #takes in a number
            strS = str(s)
            for d in strS:   #first pass just filter out strings with invalid digits
                if d not in mappings:
                    return False
            
            reverseStr = strS[::-1]  #reverse then swap with mappings
            finalStr = ''
            for c in reverseStr:
                finalStr += mappings[c]
        
            if finalStr != strS:
                return True
        
            return False
        
        self.count = 0
        def combos(n):  #takes in a number
            if n > N:
                return
            
            if isConfusingNumber(n):
                self.count += 1
            
            n = n*10
            for key in mappings:
                combos(n + int(key))
            
        combos(1)
        combos(6)
        combos(8)
        combos(9)
        return self.count