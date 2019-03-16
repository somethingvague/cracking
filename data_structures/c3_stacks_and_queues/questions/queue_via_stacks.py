"""Question 3.4

Implement a queue using 2 stacks
"""
from data_structures.c3_stacks_and_queues.stack import Stack


class QueueViaStacks:
    def __init__(self):
        """newest stack has most recent item on top, oldest has oldest item on top"""
        self.newest = Stack()
        self.oldest = Stack()

    def add(self, item):
        """Adds item to the queue

        Args:
            item: item to be added to the queue
        """
        if not self.oldest.is_empty():
            self._shift_stacks()  # Move items back to newest stack so that we can insert the item in correct place
        self.newest.push(item)

    def remove(self):
        """Removes and returns item to the queue

        Returns:
            oldest item in the queue
        Raises:
            IndexError if the queue is empty
        """
        if self.oldest.is_empty():
            self._shift_stacks()  # Move items back to oldest stack so that we can pop oldest off the top
        return self.oldest.pop()

    def _shift_stacks(self):
        """Moves items from the stack which has elements to the stack which does not"""
        from_stack, to_stack = (self.newest, self.oldest) if self.oldest.is_empty() else (self.oldest, self.newest)
        while not from_stack.is_empty():
            to_stack.push(from_stack.pop())
