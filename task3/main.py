import heapq

def dijkstra(graph):
    first = next(iter(graph))
    min_heap = [(0, first)]
    shortest_paths = {node: float('inf') for node in graph}
    shortest_paths[first] = 0
    visited = set()

    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)
        if current_node in visited:
            continue
        visited.add(current_node)
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))
    return shortest_paths

def main():
    graph = {
        'A': {'B': 2, 'C': 5, 'G': 20},
        'B': {'A': 2, 'C': 1, 'D': 7, 'G': 15},
        'C': {'A': 5, 'B': 1, 'D': 3, 'E': 9, 'F': 12},
        'D': {'B': 7, 'C': 3, 'E': 4, 'F': 6},
        'E': {'C': 9, 'D': 4, 'F': 2, 'G': 1},
        'F': {'C': 12, 'D': 6, 'E': 2, 'G': 5},
        'G': {'A': 20, 'B': 15, 'E': 1, 'F': 5}
    }
    
    shortest_paths = dijkstra(graph)
    
    print(f"Найкоротші шляхи від вершини початкової вершини:")
    for node, distance in shortest_paths.items():
        print(f"Відстань до {node}: {distance}")

if __name__ == "__main__":
    main()
