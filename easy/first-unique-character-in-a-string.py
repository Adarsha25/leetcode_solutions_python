#  https://leetcode.com/problems/first-unique-character-in-a-string/submissions/874704363/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        seen = set()
        for idx, c in enumerate(s):
            if c not in seen:
                d[c] = idx
                seen.add(c)
            elif c in d:
                del d[c]
        return min(d.values()) if d else -1