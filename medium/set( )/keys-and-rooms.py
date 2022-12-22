# https://leetcode.com/problems/keys-and-rooms/submissions/863779134/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        
        stack = [0]
        Visited = set(stack)

        while stack:
            index = stack.pop()

            for j in rooms[index]:
                if j not in Visited:
                    stack.append(j)
                    Visited.add(j)

        return len(Visited) == len(rooms)




