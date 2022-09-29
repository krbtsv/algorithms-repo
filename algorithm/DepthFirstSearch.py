graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D', 'F', 'E'],
    'D': ['B', 'C'],
    'E': ['C', 'F', 'G'],
    'F': ['C', 'E', 'G'],
    'G': ['E', 'F', 'H', 'K'],
    'H': ['G', 'K'],
    'K': ['G', 'H'],
}


def dfs(startPoint, searchPoint, graph, visited):
    if startPoint == searchPoint:
        return True
    if startPoint in visited:
        return False

    visited += [startPoint]
    for neighbour in graph[startPoint]:
        if neighbour not in visited:
            if dfs(neighbour, searchPoint, graph, visited):
                return True

    return False


print(dfs('A', 'K', graph, []))

# O(V+E)
# V - общее кол-во вершин
# E - общее кол-во ребер
