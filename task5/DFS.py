import matplotlib.pyplot as plt
from drawtree import draw_tree, generate_color

def depth_first_search(root, graph, pos):
    if not root:
        return

    stack = [root]
    visited = set()
    order = 0

    plt.ion() 

    while stack:
        node = stack.pop()
        if node and node.id not in visited:
            visited.add(node.id)
            node.color = generate_color(order, total_nodes=len(graph.nodes))
            graph.nodes[node.id]['color'] = node.color  
            order += 1

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

            draw_tree(graph, pos, title=f"DFS - Step {order}")

    plt.ioff()  