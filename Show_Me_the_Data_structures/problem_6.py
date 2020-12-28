class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        out_string += str(None)
        return out_string

    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size

    def linked_list_to_set(self):
        value_set = set()
        node = self.head
        if node is None:
            return value_set
        while node:
            value_set.add(node.value)
            node = node.next
        return value_set


def union(llist_1, llist_2):
    set1 = llist_1.linked_list_to_set()
    set2 = llist_2.linked_list_to_set()
    unified_list = LinkedList()
    for item in set1.union(set2):
        unified_list.append(item)
    return unified_list


def intersection(llist_1, llist_2):
    set1 = llist_1.linked_list_to_set()
    set2 = llist_2.linked_list_to_set()
    intersected_list = LinkedList()
    if len(set1) == 0 or len(set2) == 0:
        print("Error - intersection of a non empty set is an empty set")
        return
    for item in set1.intersection(set2):
        intersected_list.append(item)
    return intersected_list


if __name__ == "__main__":

    print("testcase 1 ----->")
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()
    element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
    for i in element_1:
        linked_list_1.append(i)

    element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]
    for i in element_2:
        linked_list_2.append(i)

    # expected : 32 -> 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 9 -> 11 -> 21
    print("union",union(linked_list_1, linked_list_2))
    # expected : 4 -> 6 -> 21
    print("intersection", intersection(linked_list_1, linked_list_2))
    print("\n***********************************************\n")

    print("testcase 2 ----->")
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()
    element_3 = []
    for i in element_3:
        linked_list_3.append(i)

    element_4 = [6, 32, 4, 9, 6, 1, 11, 21, 1]
    for i in element_4:
        linked_list_4.append(i)

    # expected : 32 -> 1 -> 4 -> 21 -> 6 -> 9 -> 11
    print("union", union(linked_list_3, linked_list_4))
    # expected : None
    print("intersection", intersection(linked_list_3, linked_list_4))
    print("\n***********************************************\n")

    print("testcase 3 ----->")
    linked_list_5 = LinkedList()
    linked_list_6 = LinkedList()
    element_5 = [2, 2, 2, 2, 2]
    for i in element_5:
        linked_list_5.append(i)

    element_6 = [2, 2, 2, 2, 2]
    for i in element_6:
        linked_list_6.append(i)

    # expected : 2
    print("union", union(linked_list_5, linked_list_6))
    # expected : 2
    print("intersection", intersection(linked_list_5, linked_list_6))

    print("\n***********************************************\n")

    print("testcase 4 ----->")
    linked_list_7 = LinkedList()
    linked_list_8 = LinkedList()
    element_7 = []
    for i in element_7:
        linked_list_5.append(i)

    element_8 = []
    for i in element_8:
        linked_list_6.append(i)

    # expected : None
    print("union", union(linked_list_7, linked_list_8))
    # expected : None
    print("intersection", intersection(linked_list_7, linked_list_8))