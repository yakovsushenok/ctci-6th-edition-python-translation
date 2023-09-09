import unittest
from src.chapter3.problems.problem_6.my_approach import Animal, AnimalShelter


class AnimalShelterTests(unittest.TestCase):
    def setUp(self) -> None:
        self.animal_shelter = AnimalShelter()
        self.cat_1 = Animal("cat")
        self.cat_2 = Animal("cat")
        self.cat_3 = Animal("cat")
        self.dog_1 = Animal("dog")
        self.dog_2 = Animal("dog")
        self.dog_3 = Animal("dog")

    def test_enqueue(self):
        # When a dog is brought to the animal shelter (we enqueue a dog),
        self.animal_shelter.enqueue(self.dog_1)
        # the dog should be pushed to both the animal queue and the dog queue
        self.assertEqual(self.animal_shelter.animal_queue.peek(), self.dog_1)
        self.assertEqual(self.animal_shelter.dog_queue.peek(), self.dog_1)
        # When a cat is brought to the animal shelter (we enqueue a cat),
        self.animal_shelter.enqueue(self.cat_1)
        # the cat should be pushed to both the animal queue and the cat queue
        self.assertEqual(
            self.animal_shelter.animal_queue.first_node.next.data, self.cat_1
        )
        self.assertEqual(self.animal_shelter.cat_queue.peek(), self.cat_1)

    def test_dequeue(self):
        self.animal_shelter.enqueue(self.cat_1)
        self.animal_shelter.enqueue(self.dog_1)
        self.animal_shelter.enqueue(self.cat_2)
        self.animal_shelter.enqueue(self.dog_2)
        # When we dequeue an animal, the one that was enqueued first should be the one to be dequeued
        dequeued_animal_1 = self.animal_shelter.dequeue()
        dequeued_animal_2 = self.animal_shelter.dequeue()
        self.assertEqual(dequeued_animal_1, self.cat_1)
        self.assertEqual(dequeued_animal_2, self.dog_1)
        # and the corresponding queue to the type of animal should have that animal removed
        self.assertEqual(self.animal_shelter.cat_queue.first_node.data, self.cat_2)
        self.assertEqual(self.animal_shelter.dog_queue.first_node.data, self.dog_2)

    def test_dequeue_cat(self):
        self.animal_shelter.enqueue(self.cat_1)
        self.animal_shelter.enqueue(self.dog_1)
        self.animal_shelter.enqueue(self.dog_2)
        # When we dequeue a cat which is the oldest animal in the shelter
        # the top of the queue should become the second animal to be enqueued
        self.animal_shelter.dequeue_cat()
        self.assertEqual(self.animal_shelter.animal_queue.peek(), self.dog_1)
        # cleaning animal shelter up
        self.animal_shelter.dequeue()
        self.animal_shelter.dequeue()
        # adding cat to be in the middle
        self.animal_shelter.enqueue(self.dog_1)
        self.animal_shelter.enqueue(self.cat_1)
        self.animal_shelter.enqueue(self.dog_2)
        # When we dequeue a cat which isn't the oldest animal in the shelter and not the youngest,
        self.animal_shelter.dequeue_cat()
        # then the animal queue should have the cat removed
        self.assertEqual(self.animal_shelter.animal_queue.first_node.data, self.dog_1)
        self.assertEqual(
            self.animal_shelter.animal_queue.first_node.next.data, self.dog_2
        )
        self.assertEqual(self.animal_shelter.animal_queue.first_node.next.next, None)
        # cleaning animal shelter up
        self.animal_shelter.dequeue()
        self.animal_shelter.dequeue()
        # adding cat to be in the middle
        self.animal_shelter.enqueue(self.dog_1)
        self.animal_shelter.enqueue(self.dog_2)
        self.animal_shelter.enqueue(self.cat_1)
        # When we dequeue a cat which is the youngest animal in the shelter
        self.animal_shelter.dequeue_cat()
        # then the animal queue should have the cat removed
        self.assertEqual(self.animal_shelter.animal_queue.first_node.data, self.dog_1)
        self.assertEqual(
            self.animal_shelter.animal_queue.first_node.next.data, self.dog_2
        )


if __name__ == "__main__":
    unittest.main()
