import networkx as nx
import matplotlib.pyplot as plt

def add_edges(graph, heap, pos, x=0, y=0, layer=1, index=0):
    if index < len(heap):
        graph.add_node(index, label=heap[index])
        
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        
        if left_index < len(heap):
            graph.add_edge(index, left_index)
            l = x - 1 / 2 ** layer
            pos[left_index] = (l, y - 1)
            add_edges(graph, heap, pos, x=l, y=y - 1, layer=layer + 1, index=left_index)
        
        if right_index < len(heap):
            graph.add_edge(index, right_index)
            r = x + 1 / 2 ** layer
            pos[right_index] = (r, y - 1)
            add_edges(graph, heap, pos, x=r, y=y - 1, layer=layer + 1, index=right_index)

def draw_heap(heap):
    graph = nx.DiGraph()
    pos = {0: (0, 0)} 
    add_edges(graph, heap, pos)
    
    labels = {node: graph.nodes[node]['label'] for node in graph.nodes}
    
    plt.figure(figsize=(10, 6))
    nx.draw(graph, pos, labels=labels, with_labels=True, node_size=2000, node_color="skyblue", font_size=12)
    plt.title("Heap Visualization as a Tree (Direct from Array)")
    plt.show()