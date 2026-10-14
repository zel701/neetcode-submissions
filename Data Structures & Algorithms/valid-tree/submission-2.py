class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n ==1:
            return True
        visited = set()
        graph = defaultdict(list)
        for root,child in edges:
            graph[root].append(child)
            graph[child].append(root)
        remain = [edges[0][0]]
        visited.add(edges[0][0])
        while remain:
            current = remain.pop()
            for i in graph[current]:
                if i not in visited:
                    remain.append(i)
                    visited.add(i)
        return len(visited) == n and len(edges) == n-1