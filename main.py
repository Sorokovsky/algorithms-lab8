def get_graph() -> dict[str, dict[str, int]]:
    return {
        'a': {'b': 6, 'c': 2, 'e': 8},
        'b': {'f': 4},
        'c': {'b': 3},
        'd': {},
        'e': {'d': 7, 'f': 1},
        'f': {'d': 2}
    }


def dijkstree(graph: dict[str, dict[str, int]], start: str, end: str) -> int:
    if start == end:
        return 0

    distances: dict[str, float] = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    visited = set()
    while True:
        current_vertex = None
        min_dist = float('inf')
        for vertex in graph:
            if vertex not in visited and distances[vertex] < min_dist:
                min_dist = distances[vertex]
                current_vertex = vertex
        if current_vertex is None:
            break
        visited.add(current_vertex)
        if current_vertex == end:
            return int(distances[current_vertex])

        for neighbor, weight in graph.get(current_vertex, {}).items():
            new_distance = distances[current_vertex] + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance

    return -1 if distances[end] == float('inf') else int(distances[end])


def floyd_warshall(graph: dict[str, dict[str, int]]) -> dict[str, dict[str, float]]:
    vertices = list(graph.keys())
    for start in graph:
        for end in graph[start]:
            if end not in vertices:
                vertices.append(end)
    distances: dict[str, dict[str, float]] = {}
    for i in vertices:
        distances[i] = {}
        for j in vertices:
            if i == j:
                distances[i][j] = 0
            elif j in graph.get(i, {}):
                distances[i][j] = graph[i][j]
            else:
                distances[i][j] = float('inf')
    for k in vertices:
        for i in vertices:
            for j in vertices:
                path = distances[i][k] + distances[k][j]
                if path < distances[i][j]:
                    distances[i][j] = path
    return distances


def task1() -> None:
    graph = get_graph()
    vertices = ['b', 'c', 'd', 'e', 'f']
    print("Пошук коротких шляхів алгоритмом Дейкстри від вершини а до всіх")
    for vertex in vertices:
        print(f"Шлях від a до {vertex} = {dijkstree(graph, 'a', vertex)}")


def task2() -> None:
    graph = get_graph()
    vertices = ['a', 'b', 'c', 'd', 'e', 'f']
    print("Шляхи від кожної до кожної вершини алгоритмом Флойда")
    distances = floyd_warshall(graph)
    for start in vertices:
        for end in vertices:
            distance = distances[start][end]
            print(f"{start}->{end} = {distance}")

def main() -> None:
    task2()

if __name__ == '__main__':
    main()
