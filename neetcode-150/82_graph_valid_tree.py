# You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.
#
# Return true if the edges of the given graph make up a valid tree, and false otherwise.
#
# Example 1:
#
# Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
# Output: true
# Example 2:
#
#
# Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
# Output: false
#
#
# Constraints:
#
# 1 <= n <= 2000
# 0 <= edges.length <= 5000
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# There are no self-loops or repeated edges.


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]

        #Number of Edges should be equal to n-1 for trees
        if len(edges) != n - 1:
            return False

        #This is undirected graph
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        visited = set()
        self.bfs(0, graph, visited)
        return len(visited) == n

    def bfs(self, node, graph, visited):
        if node in visited:
            return
        visited.add(node)
        for neighbour in graph[node]:
            self.bfs(neighbour, graph, visited)