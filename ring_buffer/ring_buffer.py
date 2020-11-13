class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.pointer = 0
        self.buffer = [None]*self.capacity

    def append(self, item):
        self.buffer[self.pointer] = item
        self.pointer += 1
        if self.pointer == self.capacity:
            self.pointer = 0

    def get(self):
        return [i for i in self.buffer if i is not None]
