import sys

class Node:
    def __init__(self, value, count=0):
        self.char = value
        self.count = count
        self.left = None
        self.right = None
        self.bit = None

    def __lt__(self, obj):
        """self < obj."""
        return self.count < obj.count


class PriorityQueue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0

    # for inserting an element in the queue
    def insert(self, data):
        self.queue.append(data)

    # for popping an element based on Priority
    def delete(self):
        try:
            self.queue.sort()
            item = self.queue[0]
            del self.queue[0]
            return item
        except IndexError:
            print()
            exit()

    def length(self):
        return len(self.queue)


def path_from_node_to_root(root, data):
    """
    :param: root - root of binary tree
    :param: data - value (representing a node)
    from root to the data node
    """
    if root is None:
        return None
    elif root.char == data:
        code = root.bit
        return [code]
    left_path = path_from_node_to_root(root.left, data)
    if left_path is not None:
        left_path.append(root.bit)
        return left_path

    right_path = path_from_node_to_root(root.right, data)
    if right_path is not None:
        right_path.append(root.bit)
        return right_path
    return None


def path_from_root_to_node(root, data):
    """
    :param data: value stored at the node.
    :return: list of nodes traveresed from a specific node with data = data to the root
    """
    output = path_from_node_to_root(root, data)
    output = "".join([str(item) for item in output if item is not None])
    return output[::-1]


def is_last(node):
    return not node.left and not node.right


def go_right(node):
    return node.right


def go_left(node):
    return node.left


def huffman_encoding(data, priorityq):
    freequency_table = dict()

    for item in data:
        if item not in freequency_table:
            freequency_table[item] = 1
        else:
            freequency_table[item] += 1

    for char in freequency_table:
        node = Node(char)
        node.count = freequency_table[char]
        priorityq.insert(node)

    while priorityq.length() > 1:
        first_node = priorityq.delete()
        first_node.bit = 0
        second_node = priorityq.delete()
        second_node.bit = 1
        value = first_node.count + second_node.count
        new_node = Node(value)
        new_node.count = value
        new_node.left = first_node
        new_node.right = second_node
        priorityq.insert(new_node)

    for char in freequency_table:
        freequency_table[char] = (freequency_table[char], path_from_root_to_node(priorityq.queue[0], char))
    print(freequency_table)

    encoded_data = ""
    for char in data:
        encoded_data += freequency_table[char][1]
    print(encoded_data)
    return encoded_data


def huffman_decoding(root, s):
    result = []
    node = root
    for char in s:
        if char == '1':
            node = go_right(node)
        elif char == '0':
            node = go_left(node)

        if is_last(node):
            result.append(node.char)
            node = root

    return ''.join(result)


if __name__ == '__main__':
    a_great_sentence = "The bird is the word"
    priorityq = PriorityQueue()

    encoded_data = huffman_encoding(a_great_sentence, priorityq)
    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(priorityq.queue[0], encoded_data)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}\n".format(decoded_data))
    print(decoded_data == a_great_sentence)