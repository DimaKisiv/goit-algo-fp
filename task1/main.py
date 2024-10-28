from linkedlist import LinkedList
from mergelists import merge_sorted_linked_lists

def main():
    llist = LinkedList()

    # Вставляємо вузли в початок
    llist.insert_at_beginning(5)
    llist.insert_at_beginning(10)
    llist.insert_at_beginning(15)

    # Вставляємо вузли в кінець
    llist.insert_at_end(20)
    llist.insert_at_end(25)

    # Друк зв'язного списку
    print("Зв'язний список:")
    llist.print_list()

    llist.reverse_list()

    print("Реверсований зв'язний список:")
    llist.print_list()

    llist.sort()
    print("Посортований зв'язний список:")
    llist.print_list()

    llist2 = LinkedList()

    llist2.insert_at_beginning(6)
    llist2.insert_at_beginning(11)
    llist2.insert_at_beginning(16)

    llist2.insert_at_end(21)
    llist2.insert_at_end(26)

    llist2.sort()
    print("Другий посортований зв'язний список:")
    llist2.print_list()

    print("Об'єднані 2 списки:")
    merged_list = merge_sorted_linked_lists(llist, llist2)
    merged_list.print_list()

if __name__ == "__main__":
    main()