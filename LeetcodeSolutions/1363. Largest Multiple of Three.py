class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        '''
        -can use a clever trick, if the sum of digits % 3 == 0, then the whole number is a multiple of 3
        -i can sort by digit DESC, then GREEDILY form combinations
        
               x
        [8,7,6,1,0]
        so start by trying 87610, i notice the sum of digits is not divisible by 3, so i drop the 0. still not %3, then i drop the 1 instead
        chunkSize = 1
        idx = n-chunkSize
        8761 = digits[0:4] + digits[5:]
        8760 = digits[0:3] + digits[4:]
        8710 = digits[0:2] + digits[3:]
        8610 = digits[0:1] + digits[2:]
        7610 = digits[0:0] + digits[1:]
        876  = digits[0:3] + digits[]
        870
        810
        610
        .
        .
        .
        .
        
        
        for chunkSize in range(1, n):  #size of the chunk to delete
            for idx in range(n-chunkSize,-1,-1):
                newList = digits[0:idx] + digits[idx + chunkSize:]
        
        
        ""  - if i end up deleting everything and I still haven't returned something yet, return empty string
        
        '''
        
        digits.sort(reverse=True)
        
        def checkValid(arr):
            if sum(arr) % 3 == 0:
                return True
            return False
            
        if checkValid(digits):
            return str(int(''.join(map(str,digits))))
        
        n = len(digits)
        for i in range(1,n): #i is the deletion chunk size
            for j in range(n-i, -1, -1):                
                newGeneratedArr = digits[0:j] + digits[j+i:]
                #print(newGeneratedArr)
                if checkValid(newGeneratedArr):
                    return ''.join(map(str,newGeneratedArr))
                
        return ""