class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)] #Initialize graph
        for prereq in prerequisites:
            graph[prereq[1]].append(prereq[0])
        visited = [False for _ in range(numCourses)] #Avoid duplicate processing
        dfs_set = set() #Identifiy cycles
        stack = []

        for course in range(numCourses):
            if not visited[course]: #if course is not visited
                if not self.dfs(course, graph, visited, dfs_set, stack): #We detected a loop
                    return []

        return stack[::-1] #Return course in reverse order


    def dfs(self, course, graph, visited, dfs_set, stack):
        visited[course] = True
        dfs_set.add(course)

        for prereq in graph[course]:
            if not visited[prereq] and not self.dfs(prereq, graph, visited, dfs_set, stack):   #If the prereq is not visited and there is a cycle starting at prereq
                return False
            if prereq in dfs_set:  #There is a loop and prereq is in dfs
                return False

        dfs_set.remove(course) #Remove the course from set
        stack.append(course) #Add Course to stack
        return True