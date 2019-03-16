"""Question 3.3

Implement a set of stacks where a new stack is start once capacity is met. Should behave like a normal stack.
"""
from data_structures.c3_stacks_and_queues.stack import Stack


class StackWithSize(Stack):
    def __init__(self):
        super().__init__()
        self.size = 0

    def push(self, data):
        super().push(data)
        self.size += 1

    def pop(self):
        self.size -= 1
        return super().pop()


class SetOfStacks:
    def __init__(self, max_stack_size):
        self.stacks = []
        self.max_stack_size = max_stack_size

    def push(self, data):
        """Adds data onto the most recent stack, adds new stack if the latest is at maximum capacity

        Args:
            data: data to put on the most recent, or new, stack
        """
        if len(self.stacks) == 0 or self.stacks[-1].size == self.max_stack_size:
            self.stacks.append(StackWithSize())
        self.stacks[-1].push(data)

    def pop(self):
        """Pops data from the most recent stack, or the one before if it is empty

        Returns:
            most recent data
        Raises:
            IndexError if there are no stacks later
        """
        if len(self.stacks) == 0:
            raise IndexError('No stack to pop from')

        if self.stacks[-1].size == 0:
            self.stacks = self.stacks[:-1]

        return self.stacks[-1].pop()
