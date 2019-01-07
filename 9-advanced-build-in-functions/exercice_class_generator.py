#!/usr/bin/env python3.7

# Prime Numbers Generator

class PrimeNumbers:
    def __init__(self, stop):
        self.stop = stop
        self.start = 2

    def __next__(self):
        for n in range(self.start, self.stop):
            for x in range(2, n):
                if n % x == 0:
                    break

            else:
                self.start = n + 1
                return n

        else:
            raise StopIteration()


g = PrimeNumbers(20)
print(g.__next__())
print(g.__next__())
print(g.__next__())
