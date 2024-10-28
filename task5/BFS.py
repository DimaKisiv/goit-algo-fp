import matplotlib.pyplot as plt
from drawtree import draw_tree, generate_color
from collections import deque

def breadth_first_search(root, graph, pos):
    if not root:
        return

    queue = deque([root])
    visited = set()
    order = 0

    plt.ion() 

    while queue:
        node = queue.popleft()
        if node and node.id not in visited:
            visited.add(node.id)
            node.color = generate_color(order, total_nodes=len(graph.nodes))
            graph.nodes[node.id]['color'] = node.color 
            order += 1

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            draw_tree(graph, pos, title=f"BFS - Step {order}")

    plt.ioff() 