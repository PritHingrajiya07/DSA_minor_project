class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def get_items(self):
        return self.items


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def get_items(self):
        return self.items

class CircularQueue:
    def __init__(self, max_size):
        self.items = [None] * max_size
        self.max_size = max_size
        self.front = self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.max_size == self.front:
            return "Queue is full"
        elif self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.max_size
        self.items[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            return None
        elif self.front == self.rear:
            item = self.items[self.front]
            self.front = self.rear = -1
        else:
            item = self.items[self.front]
            self.front = (self.front + 1) % self.max_size
        return item

    def is_empty(self):
        return self.front == -1

    def size(self):
        if self.is_empty():
            return 0
        elif self.rear >= self.front:
            return self.rear - self.front + 1
        else:
            return self.max_size - self.front + self.rear + 1

    def get_items(self):
        if self.is_empty():
            return []
        elif self.rear >= self.front:
            return self.items[self.front:self.rear + 1]
        else:
            return self.items[self.front:] + self.items[:self.rear + 1]
