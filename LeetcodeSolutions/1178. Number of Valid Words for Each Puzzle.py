class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        '''
        kind of like the anagram type of hashing? 26-tuple hashing?
        -first put all the words into a map (by doing that 26-tuple hashing)
        -then loop thru each word in puzzles and generate all subsets
        
        
        for puzzle in puzzles:
            generate all subsets of this word, must include first letter?. check if that subset is in the map
        
        '''
        #classic take/dont take to create all subsequences/subsets
        def genAllSubseqs(idx, mask):
            if idx == 7:
                if mask in myMap:
                    return myMap[mask]
                return 0
            
            tmp = 0
            #dont take
            tmp += genAllSubseqs(idx+1, mask)
            #take
            tmp += genAllSubseqs(idx+1, mask | 1<<ord(p[idx])-ord('a'))
            
            return tmp
            
            
        
        myMap = defaultdict(int)
        for w in words:
            mask = 0
            for c in w:
                mask |= 1<<ord(c)-ord('a')
            myMap[mask] += 1
        
        output = []
        for p in puzzles:
            output.append(genAllSubseqs(1, 1<<ord(p[0])-ord('a')))
        return output