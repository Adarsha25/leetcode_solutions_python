#  https://leetcode.com/problems/valid-anagram/submissions/875545952/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anag = True
        if len(s) != len(t): 
            anag = False
        else:
            letters = "abcdefghijklmnopqrstuvwxyz"
            for letter in letters:
                if s.count(letter) != t.count(letter):
                    anag = False
                    break
        return anag