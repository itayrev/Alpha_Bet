class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, node):
        if self.head is None:
            self.head = node
            return
        temp_head = self.head
        while temp_head.next is not None:
            temp_head = temp_head.next
        temp_head.next = node

    def remove_head(self):
        if self.head is None:
            return
        self.head = self.head.next

    def is_empty(self):
        if self.head is None:
            return True

    def print_list(self):
        if self.head is None:
            return
        temp_head = self.head
        while temp_head is not None:
            print(temp_head.data)
            temp_head = temp_head.next



if __name__ == '__main__':
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    l1 = LinkedList()
    l1.add_node(n1)
    l1.add_node(n2)
    l1.add_node(n3)
    l1.add_node(n4)
    # l1.print_list()
    l1.remove_head()
    l1.remove_head()
    l1.print_list()
