# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.
#
# Return the number of connected components in the graph.
#
# Example 1:
#
# Input: n = 5, edges = [[0,1],[1,2],[3,4]]
# Output: 2
# Example 2:
#
# Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
# Output: 1
#
# Constraints:
#
# 1 <= n <= 2000
# 1 <= edges.length <= 5000
# edges[i].length == 2
# 0 <= ai <= bi < n
# ai != bi
# There are no repeated edges.

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        visited = set()
        graph = [[] for _ in range(n)]

        #Construct the graph
        for edge in edges:
            graph[edge[0]].append(edge[1])

        #Loop thru the edges untill all of them are visited.
        for node in range(len(graph)) :
            if node not in visited:
                count += 1
                self.dfs(node, graph, visited)

        return count

    def dfs(self, node, graph, visited):
        if node in visited: #Assuming we dont have any cycles
            return
        visited.add(node)
        for neighbour in graph[node]:
            self.dfs(neighbour, graph, visited)

