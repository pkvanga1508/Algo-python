# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.
#
# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.
#
# Example 1:
#
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0. So it is possible.
# Example 2:
#
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take.
# To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
#
# Constraints:
#
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_graph = {}
        for prerequisite in prerequisites:
            prerequisite_courses = course_graph.get(prerequisite[0], [])
            prerequisite_courses.append(prerequisite[1])
            course_graph[prerequisite[0]] = prerequisite_courses

        visited = set()
        for course in range(numCourses):
            if not self.canFinishCourse(course, visited, course_graph):
                return False
        return True

    def canFinishCourse(self, course, visited, course_graph):

        if course in visited:
            return False #Cycle as visited

        if course not in course_graph or not course_graph[course]: #Course has no dependency or empty dependency
            return True #No Dependencies

        visited.add(course)
        for prerequisite in course_graph[course]:
            if not self.canFinishCourse(prerequisite, visited, course_graph):
                return False #Prereq can not be completed

        visited.remove(course) #Course can be finished so remove from visited
        course_graph[course] = [] #No dependencies
        return True #Finally return True - can finish course