class Solution:
    def canCross(self, stones: List[int]) -> bool:
        '''
            -need a map to store the possible jump sizes to get to that stoneNum
            
                  [0,1,3,5,6,8,12,17]
            pJ =  {0:(0)}
                  {1:(1)}
                  {3:(2)}
                  {5:(2)}   
                  {6:(3,1)}
                  {8:(3,2)}   8+(3-1) .. 8+(3)... 8+(3+1) ..        8+(2-1) ... 8+(2)  ... 8+(2+1)
                  {12:(4)}
                  {17:(5)}
                  
                  
                  [0,1,2,3,4,8,9,11]
            pJ =  {0:(0)}
                  {1:(1)} 1+(1), 1+(2)
                  {2:(1)}  2+(1), 2+(2)
                  {3:(2,1)} 3+(1), 3+(2), 3+(3)     3+(1), 3+(2)   
                  {4:(2,1)} 4+(1). 4+(2), 4+(3)     4+(1), 4+(2)
                  {8:()}
                  {9:()}
                  {11:()}
                  
                  
                  ******possibleJumps stores all the possible jump sizes to get to that stone
                  
                  ahh i see why i need to initialize the pJ mappings first beforehand.
                    its so that if the currStone + possibleJumpSizes is in the map, then i can just add
                    that jumpSize to that furtherStone's map value.
                    
                -it is critical to understand that once you iterate to a certain stone, you have already pre-filled its corresponding
                    set of possibleJumps completely. you have already found all of the possible jump sizes to get to that stone you are
                    currently on.
            
        ''' 
        possibleJumps = {}
        for num in stones:
            possibleJumps[num] = set()
        possibleJumps[0] = set([0])
        possibleJumps[1] = set([1])
        
        for i in range(1, len(stones)):
            allJumpsToGetHere = possibleJumps[stones[i]]
            for jumps in set(allJumpsToGetHere):
                low = jumps - 1
                mid = jumps
                high = jumps + 1
                if low != 0:
                    if stones[i] + low in possibleJumps:
                        possibleJumps[stones[i]+low].add(low)
                if stones[i] + mid in possibleJumps:
                    possibleJumps[stones[i]+mid].add(mid)
                if stones[i] + high in possibleJumps:
                    possibleJumps[stones[i]+high].add(high)
                
            
        print(possibleJumps)
        if possibleJumps[stones[-1]]: #this means that there were possibleJumps to get to the last stone
            return True
        return False  #this means that the last value in possibleJumps is a null set()