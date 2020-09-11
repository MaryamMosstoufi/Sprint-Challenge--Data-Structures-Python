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

tree = BSTNode('')

for name in names_1:
    tree.insert(name)


for name in names_2:
    if tree.contains(name):
        duplicates.append(name)

# runtime: 0.10765194892883301 seconds
# runtime: 0.10999011993408203 seconds
# runtime: 0.10889410972595215 seconds
end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

duplicates = [x for x in names_1 if x in names_2]
# runtime: 1.2967967987060547 seconds
# runtime: 1.30289626121521 seconds
# runtime: 1.3207600116729736 seconds

dif = set(names_1).intersection(names_2)
duplicates = list(dif)
# runtime: 0.0033071041107177734 seconds
# runtime: 0.003323078155517578 seconds
# runtime: 0.0034821033477783203 seconds
