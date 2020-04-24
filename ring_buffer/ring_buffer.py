# #### Task 1. Implement a Ring Buffer Data Structure

# A ring buffer is a non-growable buffer with a fixed size. When the ring buffer is full and a new element is inserted, the oldest element in the ring buffer is overwritten with the newest element.
# This kind of data structure is very useful for use cases such as storing logs and history information, where you typically want to store information up until it reaches a certain age,
# after which you don't care about it anymore and don't mind seeing it overwritten by newer data.

# Implement this behavior in the RingBuffer class. RingBuffer has two methods, `append` and `get`.
# The `append` method adds elements to the buffer. The `get` method, which is provided, returns all of the elements in the buffer in a list in their given order.
# It should not return any `None` values in the list even if they are present in the ring buffer.

# _You may not use a Python List in your implementation of the `append` method (except for the stretch goal)_

# *Stretch Goal*:  Another method of implementing a ring buffer uses an array (Python List) instead of a linked list.  What are the advantages and disadvantages of using this method?  What disadvantage normally found in arrays is overcome with this arrangement?

# For example:

# ```python
# buffer = RingBuffer(3)

# buffer.get()   # should return []

# buffer.append('a')
# buffer.append('b')
# buffer.append('c')

# buffer.get()   # should return ['a', 'b', 'c']

# # 'd' overwrites the oldest value in the ring buffer, which is 'a'
# buffer.append('d')

# buffer.get()   # should return ['d', 'b', 'c']

# buffer.append('e')
# buffer.append('f')

# buffer.get()   # should return ['d', 'e', 'f']
# ```


from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = DoublyLinkedList()
        self.oldest = None

    def append(self, item):

        self.oldest = self.storage.head

        if self.storage.__len__() < self.capacity:
            self.storage.add_to_tail(item)

        else:
            next_oldest = self.oldest.prev
            self.storage.delete(self.oldest)
            self.oldest = next_oldest
            self.oldest.insert_before(item)

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        current_node = self.storage.head
        while current_node is not None:
            list_buffer_contents.append(current_node.value)
            current_node = current_node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
