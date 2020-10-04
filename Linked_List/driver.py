from Linked_List import linked_list, circular_linked_list

# llist = linked_list.LinkedList()
# llist.append(1)
# llist.append(2)
# llist.append(3)
#
#
# llist.insert_after_node(llist.head.next, "D")
#
# llist.delete_node("B")
# llist.delete_node("E")
#
# llist.delete_node_at_pos(0)
#
# llist.print_list()
#
# print(llist.len_iterative())
#
# llist2 = linked_list.LinkedList()
# llist2.append(4)
# llist2.append(5)
# llist2.append(6)
#
# print(llist.sum_two_lists(llist2))

cllist = circular_linked_list.CircularLinkedList()
cllist.append(1)
cllist.append(2)
cllist.append(3)
cllist.append(4)

llist = linked_list.LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)

print(cllist.is_circular_linked_list(cllist))
print(cllist.is_circular_linked_list(llist))



