# https://leetcode.com/problems/isomorphic-strings/submissions/865168749/?envType=study-plan&id=level-1

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        def Helper(word):
            output, lookup = [], {}
            i = 1
            for w in word:
                if w not in lookup:
                    lookup[w] = i
                    i +=1
                output.append(lookup[w])
            return output

        return Helper(s) == Helper(t)

                    
        