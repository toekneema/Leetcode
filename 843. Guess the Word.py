# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

import random
class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        '''
            master.guess('oobbcc')
            
            secret     = "aabbcc"
            guessWord  = "oobbee"
            matches    = 2
            candidates = ("ddbbcc","aabbcc","zobbcc")
            
            
            -check the set again to see which words have exactly 4 matching with this one: oobbcc
            -its like a transitive property proof. we dont know the secret word, but if the guessWord has 4 matching with the secret word,
                then the secret word in the candidates list will obviously also match 4 letters with the guessWord
                
            Time complexity: O(10N) = O(N)
            Space complexity: O(10N) = O(N)
            
        '''
        
        def pruneCandidates(guessWord, matches):
            for word in set(candidates):
                count = 0
                for j in range(len(word)):
                    if word[j] == guessWord[j]:
                        count += 1
                        
                if count != matches:
                    candidates.remove(word)
        
        
        candidates = set(wordlist)
        guessWord = wordlist[0]
        
        while candidates:
            matches = master.guess(guessWord)
            if matches == 6:
                return
            candidates.remove(guessWord)
            pruneCandidates(guessWord, matches)
            
            guessWord = list(candidates)[0]