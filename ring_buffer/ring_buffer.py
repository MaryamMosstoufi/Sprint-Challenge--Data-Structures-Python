class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.counter = 0
        self.pointer = 0
        self.buffer = []
        # self.root = None

    def append(self, item):
        if self.counter < self.capacity:
            self.buffer.append(item)
            self.counter += 1
            self.pointer += 1
            # self.root = ListNode(item)
            # self.root.next = self.root
        elif self.counter >= self.capacity:
            if self.pointer == self.capacity:
                self.pointer = 0
            self.buffer[self.pointer] = item
            # current = self.root
            # dif = self.counter - self.capacity
            # if dif > 0:
            #     while dif > 0:
            #         current = current.next
            #         dif -= 1
            # current.value = item
            self.counter += 1
            self.pointer += 1

    def get(self):
        return self.buffer
