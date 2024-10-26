from .animal import Animal

class Pet(Animal):
    def __init__(self, name, birth_date, species):
        super().__init__(name, birth_date)
        self._species = species

    def make_sound(self):
        sounds = {"Dog": "Bark", "Cat": "Meow", "Hamster": "Squeak"}
        return sounds.get(self._species, "Unknown sound")
