class NumberSet:
    def __init__(self):
        self.numbers = set(range(1, 101))

    def extract(self, number):
        if not (1 <= number <= 100):
            raise ValueError("El número debe estar entre 1 y 100")
        self.numbers.remove(number)

    def find_missing(self):
        return 5050 - sum(self.numbers)
