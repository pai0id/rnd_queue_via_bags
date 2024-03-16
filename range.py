import random

def get_5_range(beg):
    return Range(beg, beg + 5)
class Range:
    def __init__(self, beg, end):
        self.beg = beg
        self.end = end

    def get_rand(self):
        return random.choice(range(self.beg, self.end))

    def get_beg(self):
        return self.beg
