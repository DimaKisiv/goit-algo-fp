def sorted_insert(sorted_head, new_node):
    if not sorted_head or new_node.data < sorted_head.data:
        new_node.next = sorted_head
        return new_node
    else:
        current = sorted_head
        while current.next and current.next.data < new_node.data:
            current = current.next
        new_node.next = current.next
        current.next = new_node
    return sorted_head

def insertion_sort(head):
    sorted_head = None
    current = head
    while current:
        next_node = current.next
        sorted_head = sorted_insert(sorted_head, current)
        current = next_node
    return sorted_head