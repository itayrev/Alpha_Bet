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



