import uuid
import networkx as nx
import matplotlib.pyplot as plt

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  
        self.id = str(uuid.uuid4())  

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(graph, pos, title="Binary Tree Visualization"):
    plt.clf() 
    colors = [graph.nodes[node]['color'] for node in graph.nodes]  
    labels = {node: graph.nodes[node]['label'] for node in graph.nodes}  

    nx.draw(graph, pos, labels=labels, node_size=2000, node_color=colors, font_size=12, font_color="black")
    plt.title(title)
    plt.draw()
    plt.pause(0.5)

def generate_color(index, total_nodes):
    intensity = int(255 * (index / total_nodes)) 
    return f"#{intensity:02X}{150:02X}{255 - intensity:02X}" 