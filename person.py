import random
from range import Range

class Person:
    def __init__(self, name, bag):
        self.name = name
        self.bag = bag

    def get_name(self):
        return self.name

    def print_person(self, file):
        file.write(f"{self.name}: ")
        begs = [str(rng.get_beg()) for rng in self.bag]
        sep = ", "
        file.write(sep.join(begs))
        file.write("\n")

    def get_num(self):
        choice = random.choice(self.bag)
        self.bag.remove(choice)
        return choice.get_rand()

    def bag_is_empt(self):
        return not self.bag

    def reset_bag(self):
        self.bag = []
        self.bag.append(Range(0, 5))
        self.bag.append(Range(5, 10))
        self.bag.append(Range(10, 15))
        self.bag.append(Range(15, 20))
