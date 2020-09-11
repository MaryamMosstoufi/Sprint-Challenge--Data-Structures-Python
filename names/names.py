import time


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value >= self.value:
            if self.right == None:
                self.right = BSTNode(value)
                return value
            else:
                return self.right.insert(value)
        if value < self.value:
            if self.left == None:
                self.left = BSTNode(value)
                return value
            else:
                return self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if target == self.value:
            return True
        elif target > self.value and self.right:
            return self.right.contains(target)
        elif target < self.value and self.left:
            return self.left.contains(target)
        else:
            return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        fn(self.value)
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)

    # Part 2 -----------------------
    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        lineup = []
        lineup.append(self)

        while len(lineup) > 0:
            next_up = lineup.pop(0)
            if next_up.left:
                lineup.append(next_up.left)
            if next_up.right:
                lineup.append(next_up.right)
            print(next_up.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        lineup = []
        lineup.append(self)

        while len(lineup) > 0:
            next_up = lineup.pop(-1)
            if next_up.left:
                lineup.append(next_up.left)
            if next_up.right:
                lineup.append(next_up.right)
            print(next_up.value)
    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        print(self.value)
        if self.left:
            self.left.pre_order_dft()
        if self.right:
            self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self):
        if self.left:
            self.left.post_order_dft()
        if self.right:
            self.right.post_order_dft()
        print(self.value)


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()
# list_1 = open("names_1.txt").read().splitlines()
# list_2 = open("names_2.txt").read().splitlines()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

unique = BSTNode('')

for name in names_1:
    unique.insert(name)


for name in names_2:
    if unique.contains(name):
        duplicates.append(name)

# runtime: 0.11041688919067383 seconds
# runtime: 0.11278533935546875 seconds
# runtime: 0.10889410972595215 seconds
end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
print(duplicates)

# duplicates = [x for x in names_1 if x in names_2]
# runtime: 1.2967967987060547 seconds
# runtime: 1.30289626121521 seconds
# runtime: 1.3207600116729736 seconds

# duplicates = set(names_1).intersection(names_2)
# runtime: 0.0033071041107177734 seconds
# runtime: 0.003323078155517578 seconds
# runtime: 0.0034821033477783203 seconds
