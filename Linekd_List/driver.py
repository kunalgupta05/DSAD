from Linekd_List.linked_list import LinkedList

llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)


llist.insert_after_node(llist.head.next, "D")

llist.delete_node("B")
llist.delete_node("E")

llist.delete_node_at_pos(0)

llist.print_list()

print(llist.len_iterative())

llist2 = LinkedList()
llist2.append(4)
llist2.append(5)
llist2.append(6)

print(llist.sum_two_lists(llist2))




