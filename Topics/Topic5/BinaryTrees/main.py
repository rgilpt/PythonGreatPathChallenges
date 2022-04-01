

my_list = [45, 23, 32, 99, 2, 4, 6, 1, 5, 57, 3]


class Node:
    left_node = None
    right_node = None
    search_value = 50
    store_object = None

    def __init__(self, search_value):
        self.search_value = search_value

    def add_node(self, new_node):
        if new_node.search_value <= self.search_value:
            if self.left_node is not None:
                self.left_node.add_node(new_node)
            else:
                self.left_node = new_node

        else:
            if self.right_node is not None:
                self.right_node.add_node(new_node)
            else:
                self.right_node = new_node

    def print_node(self):
        # print(self.search_value)
        left_search_value = -1
        right_search_value = -1
        if self.left_node is not None:
            left_search_value = self.left_node.search_value
            self.left_node.print_node()
        if self.right_node is not None:
            right_search_value = self.right_node.search_value
            self.right_node.print_node()
        if left_search_value != -1 or right_search_value != -1:
            print(str(self.search_value) + ": " + (str(left_search_value) if left_search_value != -1 else "") + " --- " + (str(right_search_value) if right_search_value != -1 else ""))


def main():
    root_node = Node(my_list[0])
    del my_list[0]
    for n in my_list:
        root_node.add_node(Node(n))

    root_node.print_node()


if __name__ == '__main__':
    main()