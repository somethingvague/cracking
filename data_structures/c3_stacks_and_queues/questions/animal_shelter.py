"""Question 3.6

Implement an animal shelter queue where oldest animal has to be taken, or oldest preferred animal type
"""
from abc import ABC

from data_structures.c2_linked_lists.linked_list import LinkedList
from data_structures.c2_linked_lists.linked_list import Node


class Animal(ABC):
    def __init__(self, name):
        self.order = None
        self.name = name


class Dog(Animal):
    pass


class Cat(Animal):
    pass


class AnimalShelter:
    def __init__(self):
        self.dogs = LinkedList()
        self.cats = LinkedList()
        self.order = 0

    def enqueue(self, animal):
        """Welcomes a new animal to shelter by assigning an order and enqueueing it to the appropriate list

        Args:
            animal: animal to be added
        """
        if isinstance(animal, Dog):
            self._enqueue_to_list(animal, self.dogs)
        elif isinstance(animal, Cat):
            self._enqueue_to_list(animal, self.cats)
        # else animal is rejected :(

    def dequeue_cat(self):
        return self._dequeue_from(self.cats)

    def dequeue_dog(self):
        return self._dequeue_from(self.dogs)

    def dequeue_any(self):
        """Returns the oldest animal in the shelter"""
        oldest_cat_order = -1 if self.cats.head is None else self.cats.head.data.order
        oldest_dog_order = -1 if self.dogs.head is None else self.dogs.head.data.order
        if oldest_cat_order < oldest_dog_order:
            return self.dequeue_cat()
        else:
            return self.dequeue_dog()

    def _enqueue_to_list(self, animal, animal_list):
        """
        Args:
            animal: animal to append to the list
            animal_list: linked list to append to
        """
        animal.order = self.order
        animal_node = Node(animal)

        if animal_list.head is None:
            animal_list.head = animal_node
        else:
            animal_list.head.append_to_tail(animal_node)

        self.order += 1

    @staticmethod
    def _dequeue_from(animal_list):
        if animal_list.head is None:
            raise RuntimeError('No animals')

        animal = animal_list.head.data
        animal_list.head = animal_list.head.next
        return animal
