# https://leetcode.com/problems/keys-and-rooms/submissions/863785569/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def dfs(room): 
            visited.add(room)           
            for i in rooms[room]:
                if i not in visited:
                    dfs(i)
        dfs(0)

        return len(visited) == len(rooms)