import networkx as nx
import matplotlib.pyplot as plt
from drawtree import Node, add_edges
from BFS import breadth_first_search
from DFS import depth_first_search
   
def create_tree():
    root = Node(0)
    root.left = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(10)
    root.right = Node(1)
    root.right.left = Node(3)
    return root

def main():
    root = create_tree()
    graph = nx.DiGraph()
    pos = {root.id: (0, 0)}
    graph = add_edges(graph, root, pos)
    depth_first_search(root, graph, pos)

    root = create_tree()  
    graph = nx.DiGraph()  
    pos = {root.id: (0, 0)}
    graph = add_edges(graph, root, pos)  
    breadth_first_search(root, graph, pos)

    plt.show()

if __name__ == "__main__":
    main()
