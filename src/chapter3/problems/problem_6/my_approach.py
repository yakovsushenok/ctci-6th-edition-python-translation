from src.chapter3.my_queue import MyQueue


class Animal:
    def __init__(self, type: str) -> None:
        self.type = type


class AnimalShelter:
    def __init__(self):
        self.animal_queue = MyQueue()
        self.cat_queue = MyQueue()
        self.dog_queue = MyQueue()

    def enqueue(self, animal: Animal) -> None:
        self.animal_queue.add(animal)
        if animal.type == "cat":
            self.cat_queue.add(animal)
        else:
            self.dog_queue.add(animal)

    def dequeue(self) -> Animal:
        animal_adopted = self.animal_queue.remove()
        for queue in [self.cat_queue, self.dog_queue]:
            if not queue.is_empty() and animal_adopted == queue.peek():
                queue.remove()
        return animal_adopted

    def dequeue_cat(self) -> Animal:
        cat_adopted = self.cat_queue.remove()
        self.remove_from_animal_queue(cat_adopted)
        return cat_adopted

    def dequeue_dog(self) -> Animal:
        dog_adopted = self.dog_queue.remove()
        self.remove_from_animal_queue(dog_adopted)
        return dog_adopted

    def remove_from_animal_queue(self, animal: Animal) -> None:
        current_animal = self.animal_queue.first_node
        if current_animal.data == animal:
            return self.animal_queue.remove()
        while current_animal.next.data != animal:
            current_animal = current_animal.next
        current_animal.next = current_animal.next.next
