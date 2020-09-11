class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.counter = 0
        self.pointer = 0
        self.buffer = []

    def append(self, item):
        if self.counter < self.capacity:
            self.buffer.append(item)
            self.counter += 1
            self.pointer += 1
        elif self.counter >= self.capacity:
            if self.pointer == self.capacity:
                self.pointer = 0
            self.buffer[self.pointer] = item
            self.counter += 1
            self.pointer += 1

    def get(self):
        return(self.buffer)
