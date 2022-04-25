nodes = ('A', 'B', 'C', 'D', 'E', 'F')

distances = {
    'A': {'C': 2, 'B': 5},
    'B': {'A': 5, 'D': 8, 'C': 7},
    'C': {'A': 2, 'E': 8, 'D': 4, 'B': 7},
    'D': {'B': 8, 'C': 4, 'E': 6, 'F': 4},
    'E': {'F': 3, 'D': 6, 'C': 8},
    'F': {'D': 4, 'E': 3}
}

def find_route(current, end):
    unvisited = {node: float('inf') for node in nodes}
    current_distance = 0
    unvisited[current] = current_distance
    visited, parents = {}, {}
    while unvisited:
        min_vertex = min(unvisited, key=unvisited.get)
        for neighbour, distance in distances[current].items():
            if neighbour not in unvisited: 
                continue
            new_distance = current_distance + distance
            if unvisited[neighbour] is float('inf') or unvisited[neighbour] > new_distance:
                unvisited[neighbour] = new_distance
                parents[neighbour] = min_vertex
        visited[current] = current_distance
        unvisited.pop(min_vertex)
        if min_vertex == end: 
            break
        candidates = [node for node in unvisited.items() if node[1]]
        current, current_distance = min(candidates, key=lambda x: x[1])
    return parents, visited

def generate_path(parents, start, end):
    path = [end]
    while True:
        key = parents[path[0]]
        path.insert(0, key)
        if key == start:
            break
    return ' → '.join(path)

start, end = 'A', 'F'
parents, visited = find_route(start, end)
path = generate_path(parents, start, end)
print(f'Menor caminho: {path}')