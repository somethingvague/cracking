import unittest

from data_structures.c3_stacks_and_queues.questions.animal_shelter import AnimalShelter, Cat, Dog


class TestAnimalShelter(unittest.TestCase):
    def test_dequeue_raises_RuntimeError_when_list_is_empty(self):
        with self.assertRaises(RuntimeError):
            AnimalShelter().dequeue_any()

    def test_dequeue_cat_returns_oldest_cat(self):
        shelter = AnimalShelter()
        first_cat = Cat('Tommy')
        shelter.enqueue(Dog('Henry'))
        shelter.enqueue(first_cat)
        shelter.enqueue(Cat('Chloe'))
        self.assertEqual(shelter.dequeue_cat(), first_cat)

    def test_dequeue_dog_returns_oldest_dog(self):
        shelter = AnimalShelter()
        first_dog = Dog('Billy')
        shelter.enqueue(Cat('Toomy'))
        shelter.enqueue(first_dog)
        shelter.enqueue(Dog('Henry'))
        self.assertEqual(shelter.dequeue_dog(), first_dog)

    def test_dequeue_any_returns_oldest_animal(self):
        shelter = AnimalShelter()
        oldest = Cat('Tommy')
        shelter.enqueue(oldest)
        shelter.enqueue(Cat('Chloe'))
        shelter.enqueue(Dog('Billy'))
        self.assertEqual(shelter.dequeue_any(), oldest)


if __name__ == 'main':
    unittest.main()
