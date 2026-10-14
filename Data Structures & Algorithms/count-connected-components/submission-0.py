class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        unvisited = [x for x in range(n)]
        graph = defaultdict(list)
        for root,child in edges:
            graph[root].append(child)
            graph[child].append(root)
        visited = set()
        count = 0
        stack = []
        for i in unvisited:
            if i not in visited:
                visited.add(i)
                stack.append(i)
                count+=1
                while stack:
                    current = stack.pop()
                    for j in graph[current]:
                        if j not in visited:
                            stack.append(j)
                            visited.add(j)
        return count

        