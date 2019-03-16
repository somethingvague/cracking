"""Question 3.2

Implement a stack with a 'min' function where push, pop and min all have 0(1) time
"""


class NodeWithMin:
    """Node which forms the link in a list, with an attribute representing the current minimum in that list"""
    def __init__(self, data, minimum):
        self.data = data
        self.minimum = minimum
        self.next = None


class StackWithMin:
    def __init__(self):
        self._top = None

    def push(self, data):
        """Pushes a node, which knows the minimum data in the stack, onto a stack

        Args:
            data: data to be wrapped in a node and added to a stack
        """
        if self._top is None:
            self._top = NodeWithMin(data, data)
        else:
            existing_top = self._top
            minimum = min(existing_top.minimum, data)
            self._top = NodeWithMin(data, minimum)
            self._top.next = existing_top

    def pop(self):
        """Returns data from the top of the stack and removes it from the stack

        Raises:
            IndexError if the stack is empty
        """
        if self._top is None:
            raise IndexError('Stack is empty')

        popped_data = self._top.data
        self._top = self._top.next
        return popped_data

    def min(self):
        """Returns the minimum data in the stack"""
        return self._top.minimum
