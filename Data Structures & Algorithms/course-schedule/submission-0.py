class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for course,pre in prerequisites:
            graph[pre].append(course)
            indegree[course]+=1

        finished = 0
        class_can_take = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                class_can_take.append(i)
        while class_can_take:
            current = class_can_take.popleft()
            finished+=1
            for i in graph[current]:
                indegree[i]-=1
                if indegree[i] == 0:
                    class_can_take.append(i)
        return finished == numCourses
