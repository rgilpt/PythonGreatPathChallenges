import random

my_list = [3, 5, 1, 9]

def rand_list(number_to_add):
    for n in range(number_to_add):

        my_list.append(random.randint(0, 100000))


def find_list(number_to_find):
    count = 0
    for n in my_list:
        if n == number_to_find:
            print("found")
            count += 1
    if count == 0:
        print("not found")
    else:
        print(count)



class Node:
    left_node = None
    right_node = None
    search_value = 5
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

    def search_my_value(self, my_value):
        if self.search_value == my_value:
            return True
        if self.left_node is Node and self.right_node is None:
            return False

        if self.left_node is not None:
            if self.left_node.search_my_value(my_value):
                return True
        if self.right_node is not None:
            return self.right_node.search_my_value(my_value)


def main():
    rand_list(100000)
    root_node = Node(my_list[0])
    del my_list[0]
    for n in my_list:
        root_node.add_node(Node(n))

    find_list(405)
    print(root_node.search_my_value(405))

    # root_node.print_node()


if __name__ == '__main__':
    main()