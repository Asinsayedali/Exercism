class Node:
    def __init__(self, value=None):
        self.value_node = value
        self.next_node = None

    def value(self):
        return self.value_node

    def next(self):
        return self.next_node


class LinkedList:
    def __init__(self, values=None):
        values = values or []
        self.values = values
        self.size = 0
        self.headpoint = None
        for value in values:
            self.push(value)

    def __len__(self):
        return self.size

    def head(self):
        if self.size == 0:
            raise EmptyListException("The list is empty.")
        else:
            return self.headpoint

    def __iter__(self):
        current = self.headpoint
        while current:
            yield current.value_node
            current = current.next_node

    def push(self, value):
        if self.size == 0:
            newnode = Node(value)
            self.headpoint = newnode

        else:
            newnode = Node(value)
            newnode.next_node = self.headpoint
            self.headpoint = newnode
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise EmptyListException("The list is empty.")
        else:
            data = self.headpoint.value_node
            self.headpoint = self.headpoint.next_node
            self.size -= 1
            return data

    def reversed(self):
        reversed_list = LinkedList()
        for value in self:
            reversed_list.push(value)
        return reversed_list


class EmptyListException(Exception):
    def __init__(self, message):
        super().__init__(message)
