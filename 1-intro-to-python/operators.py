class Person:
    def __init__(self, name: str, favoriteMovie:str):
        self.name = name
        self.favoriteMovie = favoriteMovie

    def plus(cls, self):
        return f'{cls.name} and {self.name}'



ric = Person("Ricardo", "Lot")
eri = Person("Erika", "Shrek")

print(ric.plus(eri))
