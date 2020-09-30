from Linekd_List.linked_list import LinkedList

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")

llist.insert_after_node(llist.head.next, "D")

llist.delete_node("B")
llist.delete_node("E")

llist.delete_node_at_pos(0)

llist.print_list()
