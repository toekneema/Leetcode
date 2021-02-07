class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        '''
        -math problem, work backwards, modulo variant
         
        (x+y, y)   or   (x, x+y)   
        
        
        source = 2,5     target = 19,12
        
                            
                            2,5
                            /\
                        7,5   2,7
                        /\
                   12,5  7,12
                          /\
                     19,12   7,19
                     
              
              if tx > ty:
                tx %= ty
              elif ty > tx:
                ty -= tx 
              
              
              
              
              
              
              source = 1,9       target = 100,9
                           
                           
                           1,9
                           /\
                        10,9  1,10
                        /\
                   19,9    10,19
                    /\
                28,9  19,28
                /\
            37,9  28,37
            /\
          46,9  37,46
          /  \
         55,9  46,55
        / \
        ...
       .....
       82,9
       /  \
     91,9
     /    \
    100,9  91,100
                 
                 
                                
                    source = 3,3      target = 21,9            
                    
                                 3,3
                                /   \
                              6,3   3,6
                                    /   \
                                  9,6    3,9
                                  / \     /  \   
                             15,6  9,15  12,9  3,12
                                         / \
                                      21,9  12,21   
                        
                        
                        
                        
                        1) x=21, y=9
                        2) x=3, y=9
                        3) 9%=3 = 3
                        
                        
                        sx,sy (3,3)
                        
                               3,3
                               3,6
                        tx,ty (3,9)
                        
                        
                        9-3 = 6%3 == 0, return True
                        
                        
                        
                        sx,sy (3,2)
                               5,2
                               7,2
                               9,2
                        tx,ty (11,2)
                        
                        11-3 = 8%2 == 0, its V
                     
        
        '''
        while tx >= sx and ty >= sy:
            if tx==sx and ty==sy:
                return True
            
            if tx > ty:
                tx %= ty
            else:
                ty %= tx
                
            if tx == sx: #then only need to change ty
                if (ty-sy) % tx == 0:
                    return True
                else:
                    return False
                
            if ty == sy: #then only need to change tx
                if (tx-sx) % ty == 0:
                    return True
                else:
                    return False
                
        return False
                