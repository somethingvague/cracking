"""Question 3.1
Describe how you could use a single array to implement 3 stacks
"""


class ThreeInOne:
    """Wraps an array. Each stack has its own portion of the array"""

    def __init__(self, max_stack_size):
        """Initialises the store list which holds values and a list representing current size of each stack"""
        number_of_stacks = 3
        self.max_stack_size = max_stack_size
        self.store = [None] * number_of_stacks * max_stack_size
        self.stack_sizes = [0] * number_of_stacks

    def push(self, stack_index, data):
        """Pushes data to the stack at the given stack_index

        Args:
            stack_index: index of the stack to be added to
            data: data to be added the stack
        Raises:
            IndexError if the stack at the given index is already full
        """
        if self.stack_sizes[stack_index] == self.max_stack_size:
            raise IndexError('Stack {} is full'.format(stack_index))

        self.store[self._index_of_top(stack_index) + 1] = data
        self.stack_sizes[stack_index] += 1

    def pop(self, stack_index):
        """Removes and returns top the stack identified by the stack_index

        Args:
            stack_index: index of the stack from which to pop
        Returns:
            data at the top of the stack
        Raises:
            IndexError if the stack is empty
        """
        self._raise_if_empty(stack_index)
        top_index = self._index_of_top(stack_index)
        popped_data = self.store[top_index]
        self.store[top_index] = None  # reset the top
        self.stack_sizes[stack_index] -= 1  # decrement the top
        return popped_data

    def peek(self, stack_index):
        """Returns the data at the top of the stack identified by the stack_index

        Args:
            stack_index: the index of the stack from which to peek
        Returns:
            the data at the top of the stack
        Raises:
            IndexError if the stack is empty
        """
        self._raise_if_empty(stack_index)
        return self.store[self._index_of_top(stack_index)]

    def is_empty(self, stack_index):
        """
        Args:
            stack_index: the index of the stack from which to check
        Returns:
            true if the stack at the given index is empty
        """
        return self.stack_sizes[stack_index] == 0

    def _index_of_top(self, stack_index):
        """
        Args:
            stack_index: the index of the stack to retrieve the top index of
        Returns:
            the index of the top of the stack identified by the stack_index
        """
        offset = stack_index * self.max_stack_size
        return offset + self.stack_sizes[stack_index] - 1

    def _raise_if_empty(self, stack_index):
        if self.stack_sizes[stack_index] == 0:
            raise IndexError('Stack {} is empty'.format(stack_index))
