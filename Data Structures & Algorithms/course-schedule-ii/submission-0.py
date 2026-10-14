class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        order = []
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
            order.append(current)
            finished+=1
            for i in graph[current]:
                indegree[i]-=1
                if indegree[i] == 0:
                    class_can_take.append(i)
        if finished == numCourses:
            return order
        return []