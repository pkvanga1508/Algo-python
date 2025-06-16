class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        queue = []
        large_val = (2 ** 31) - 1
        for row in range(len(rooms)):
            for col in range(len(rooms[0])):
                if rooms[row][col] == 0: #Gate
                    queue.append([row, col]) #Adding all gates


        visited = []
        while queue:
            row, col = queue.pop(0)
            if rooms[row][col] == 0: #Gate
                visited = [[False for _ in range(len(rooms[0]))] for _ in range(len(rooms))]

            if row - 1 >= 0:
                if visited[row - 1][col] or rooms[row - 1][col] == 0 or rooms[row - 1][col] == -1: #Already visited or its a Wall continue
                    continue
                elif rooms[row][col] == 0: #Next to Gate
                    rooms[row - 1][col] = 1
                elif rooms[row - 1][col] == large_val: #Empty
                    rooms[row - 1][col] = rooms[row][col] + 1
                else: #THis is already processed by another gate, we just want smallest path
                    rooms[row - 1][col] = min(rooms[row - 1][col], rooms[row][col] + 1)
                queue.append([row - 1, col])
                visited[row - 1][col] = True

            if col - 1 >= 0:
                if visited[row][col - 1] or rooms[row][col - 1] == 0 or rooms[row][col - 1] == -1: #Already visited or its a Wall or Gate continue
                    continue
                elif rooms[row][col] == 0: #Next to Gate
                    rooms[row][col - 1] = 1
                elif rooms[row][col - 1] == large_val: #Empty
                    rooms[row][col - 1] = rooms[row][col] + 1
                else: #THis is already processed by another gate, we just want smallest path
                    rooms[row][col - 1] = min(rooms[row][col - 1], rooms[row][col] + 1)
                queue.append([row, col - 1])
                visited[row][col - 1] = True


            if row + 1 < len(rooms):
                if visited[row + 1][col] or rooms[row + 1][col] == 0 or rooms[row + 1][col] == -1: #Already visited or its a Wall or Gate continue
                    continue
                elif rooms[row][col] == 0: #Next to Gate
                    rooms[row + 1][col] = 1
                elif rooms[row + 1][col] == large_val: #Empty
                    rooms[row + 1][col] = rooms[row][col] + 1
                else: #THis is already processed by another gate, we just want smallest path
                    rooms[row + 1][col] = min(rooms[row + 1][col], rooms[row][col] + 1)
                queue.append([row + 1, col])
                visited[row + 1][col] = True


            if col + 1 < len(rooms[0]):
                if visited[row][col + 1] or rooms[row][col + 1] == 0 or rooms[row][col + 1] == -1: #Already visited or its a Wall or Gate continue
                    continue
                elif rooms[row][col] == 0: #Next to Gate
                    rooms[row][col + 1] = 1
                elif rooms[row][col + 1] == large_value: #Next to Gate
                    rooms[row][col + 1] = rooms[row][col] + 1
                else: #THis is already processed by another gate, we just want smallest path
                    rooms[row][col + 1] = min(rooms[row][col + 1], rooms[row][col] + 1)
                queue.append([row, col + 1])
                visited[row][col + 1] = True

        return queue


#################

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        queue = []
        large_val = (2 ** 31) - 1
        for row in range(len(rooms)):
            for col in range(len(rooms[0])):
                if rooms[row][col] == 0: #Gate
                    queue.append([row, col]) #Adding all gates


        visited = []
        while queue:
            row, col = queue.pop(0)
            if row - 1 >= 0:
                if rooms[row - 1][col] == large_val:
                    rooms[row - 1][col] = rooms[row][col] + 1
                    queue.append([row - 1, col])
            if col - 1 >= 0:
                if rooms[row][col - 1] == large_val:
                    rooms[row][col - 1] = rooms[row][col] + 1
                    queue.append([row, col - 1])

            if row + 1 < len(rooms):
                if rooms[row + 1][col] == large_val:
                    rooms[row + 1][col] = rooms[row][col] + 1
                    queue.append([row + 1, col])

            if col + 1 < len(rooms[0]):
                if rooms[row][col + 1] == large_val:
                    rooms[row][col + 1] = rooms[row][col] + 1
                    queue.append([row, col + 1])

        return rooms