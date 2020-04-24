

# *Stretch Goal*:  Another method of implementing a ring buffer uses an array (Python List) instead of a linked list.  What are the advantages and disadvantages of using this method?  What disadvantage normally found in arrays is overcome with this arrangement?

# I think using an array would be ok as long as you set the length of the array equal to the capacity at the start, and you never increased that array's length
# The disadvantage of arrays is they're expensive to increase the size of. A linked list would allow someone to change the capacity of a give list with more efficiency
# The advantage of arrays is that programmers have access to a node's index


from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = DoublyLinkedList()
        self.oldest = None

    def append(self, item):
        if self.storage.__len__() < self.capacity:
            self.storage.add_to_tail(item)
            self.oldest = self.storage.head

        else:
            the_oldest = self.oldest
            if the_oldest.next is not None:
                next_oldest = the_oldest.next
                next_oldest.insert_before(item)
                self.storage.delete(the_oldest)
                self.storage.length = self.capacity
                self.oldest = next_oldest
            else:
                self.storage.remove_from_tail()
                self.storage.add_to_tail(item)
                self.oldest = self.storage.head

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
