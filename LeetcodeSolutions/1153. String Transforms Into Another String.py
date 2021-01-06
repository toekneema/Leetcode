class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        '''
            str1 = "aabcc", str2 = "ccdee"
            map = {a : c}
                  
            
                  
            str1 = "ball", str2 = "perk"
            map = {b : p}
                  {a : e}
                  {l : r}
                  
                  
                  
            
            GRAPH representation: each > carrot represents the idea that the firstChar is transforming into the secondChar
            
            b > p
            a > e
            
            k
            ^
            l > r
            
            
            
                  
            since 'l' already maps to 'r', then we check if that existing value equals the value in str2,
                and it doesn't match, so return false
            
            
            'ybcdezferwfewfy..z'    'zfdsfdfsd...a'
            
            'ba'   'ba'
            
            str1 = 'abcdefghijklmnopqrstuvwxyz', str2 = 'zyxwvutsrqponmlkjihgfedcba'
            this is an edge case where all 26 letters are used, and in diff orders for both strings,
            this should return False obv because we can't convert any more letters
            
        '''
        
        if str1 == str2:
            return True
        
        mappings = {}
        s2set = set()
        
        for i in range(len(str1)):
            c1 = str1[i]
            c2 = str2[i]
            s2set.add(c2)
            
            if c1 not in mappings:
                mappings[c1] = c2
            else:
                if mappings[c1] != c2:
                    return False
        
        if len(mappings) == 26 and len(s2set) == 26:
            return False
        
        return True
        
        