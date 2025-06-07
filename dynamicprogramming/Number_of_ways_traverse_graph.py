## Given a grid of size width x height, find the number of ways to traverse the graph
# Problem: Given a grid of size width x height, find the number of ways to traverse the graph from the top-left corner to the bottom-right corner.
# The only allowed moves are to the right or down.
# The function should return the number of unique paths from the top-left corner to the bottom-right corner.
def numberOfWaysToTraverseGraph(width, height):

    memory = [[0 for _ in range(width)] for _ in range(height)]
    for index in range(len(memory)):
        memory[index][0] = 1
    for index in range(len(memory[0])):
        memory[0][index] = 1

    for row in range(1, len(memory)):
        for col in range(1, len(memory[0])):
            memory[row][col] = memory[row - 1][col] + memory[row][col -1]

    return memory[-1][-1]
