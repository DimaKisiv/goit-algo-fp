import heapq
from drawheap import draw_heap
from drawtree import Node, draw_tree

# функція перетворює купу в дерево
def make_tree_from_heap(heap):
    nodes = [Node(key) for key in heap]
    
    for i in range(len(nodes)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(nodes):
            nodes[i].left = nodes[left_index]
        if right_index < len(nodes):
            nodes[i].right = nodes[right_index]
    
    return nodes[0] if nodes else None

def main():
    # створюмо довільний масив
    heap_array = [10, 20, 15, 6, 22, 30, 40, 5, 7, 45, 18]
    
    # перетворюємо його в купу
    heapq.heapify(heap_array) 
    print("Купа:", heap_array)
    
    # вимальовуємо купу у вигляді дерева
    draw_heap(heap_array)

    # або спочатку перетворюємо купу на дерево і тоді вимальовуємо за допомогою коду з завдання
    tree = make_tree_from_heap(heap_array)
    draw_tree(tree)

if __name__ == "__main__":
    main()