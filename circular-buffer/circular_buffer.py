class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """

    def __init__(self, message):
        self.message = message


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """

    def __init__(self, message):
        self.message = message


class CircularBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []

    def read(self):
        if len(self.queue) == 0:
            raise BufferEmptyException("Circular buffer is empty")
        else:
            return self.queue.pop(0)

    def write(self, data):
        if len(self.queue) < self.capacity:
            self.queue.append(data)
        else:
            raise BufferFullException("Circular buffer is full")

    def overwrite(self, data):
        if len(self.queue) == self.capacity:
            self.queue.pop(0)
            self.queue.append(data)
        else:
            self.queue.append(data)

    def clear(self):
        self.queue = []
