from linkedlist import Node, LinkedList

def merge_sorted_linked_lists(list1, list2):
    temp = Node()
    tail = temp

    cur1 = list1.head
    cur2 = list2.head

    while cur1 and cur2:
        if cur1.data < cur2.data:
            tail.next = cur1
            cur1 = cur1.next
        else:
            tail.next = cur2
            cur2 = cur2.next
        tail = tail.next

    if cur1:
        tail.next = cur1
    else:
        tail.next = cur2

    return LinkedList(temp.next)