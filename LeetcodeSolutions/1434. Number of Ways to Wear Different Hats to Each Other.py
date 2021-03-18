class Solution:
    def numberWays(self, hats: List[List[int]]) -> int:
        '''
        -very similar to the campus bikes II
        -n! problem
        -so just go thru all the people in hats
            -then go thru all the preferred hats for that person
                -if the hat has already been chosen, then just continue
                -else, i will mask that hat
                
        [[3,4],[4,5],[5]]
        10000
        
        
        shoot, so now i need to do it backwards instead actually
        -i need to assign HATS to people, instead of PEOPLE to hats
        
        so my map looks like this:
        -key = hat number:
        -value = peopleIds that like that hat
        
                
        '''
        @cache
        def dfs(idx, mask):
            # if it reaches the end, it was a valid ordering
            #print(path)
            if mask == allUsedMask:
                return 1
            if idx == len(mappings):
                return 0
            
            tmp = 0
            #dont take this hat at all
            tmp += dfs(idx+1, mask)
            
            
            # take this hat
            for person in mappings[idx][1]:
                # if already used that person, then continue
                if mask & 1<<person:
                    continue
                # havent used that hat yet, so add to mask and dfs to next person
                tmp += dfs(idx+1, mask | 1<<person)
            
            # so basically after that for loop, tmp will have summed up the paths which all take a different hat
            return tmp % 1_000_000_007
        
        
        
        mappings = defaultdict(list)
        for i,prefs in enumerate(hats):
            for hat in prefs:
                mappings[hat].append(i)
        mappings = list(mappings.items())
        #print(mappings)
        
        totalPpl = len(hats)
        allUsedMask = (1<<totalPpl) - 1 #n 1s, meaning all people were succesfully paired up
        return dfs(0, 0)