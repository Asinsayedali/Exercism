class Node:
    def __init__(self, value=None, next_node_value=None):
        self.value_node = value
        self.next_node = next_node_value

    def value(self):
        return self.value_node

    def next(self):
        return self.next_node


class LinkedList:
    def __init__(self, values=None):
        self.size = 0
        self.headpoint = None
        for value in values or []:
            self.push(value)

    def __len__(self):
        return self.size

    def head(self):
        if self.size == 0:
            raise EmptyListException("The list is empty.")
        return self.headpoint

    def __iter__(self):
        current = self.headpoint
        while current:
            yield current.value_node
            current = current.next_node

    def push(self, value):
        self.headpoint = Node(value, self.headpoint)
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise EmptyListException("The list is empty.")
        data = self.headpoint.value_node
        self.headpoint = self.headpoint.next_node
        self.size -= 1
        return data

    def reversed(self):
        return LinkedList(self)


class EmptyListException(Exception):
    pass
