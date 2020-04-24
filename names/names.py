import time



# ANSWERS TO README QUESTIONS
# The runtime before I fixed it was O(n^2) because in the worst case it woiuld have had to go through a list n * n times

# Now that I fixed it it rns a lot faster. It's O (n log(n)) because worse case scenario it goes through the first list once and then it goes through the second list log(n) times because it cuts the list in half with every search

class BinarySearchTree:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # self.left and/or self.right need to be valid nodes
        # for us to call 'insert' on them

        if value < self.value:
            # check if self.left is a valid node
            if self.left:
                self.left.insert(value)
            # the left side is empty
            else:
                # we've found a valid parking spot
                self.left = BinarySearchTree(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        else:
            # or recurse to the right
            if self.right:
                return self.right.contains(target)
            else:
                return False

    def return_root_value(self):
        print(self.value)
        return self.value
    # Return the maximum value found in the tree

    def for_each(self, cb):

        if self.right:
            self.right.for_each(cb)

        cb(self.value)

        if self.left:
            self.left.for_each(cb)

    def add_list(self, list):
        for element in list:
            self.insert(element)

    def in_order_print(self, node=None):
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()

    def check_list_for_duplicates(self, list):
        for element in list:
            if self.contains(element):
                duplicates.append(element)
        return duplicates


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements

# make a bst
bst = BinarySearchTree("Joscelyn Stancek")

# add all of names_1 to my bst
bst.add_list(names_1)

# get duplicates
bst.check_list_for_duplicates(names_2)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
