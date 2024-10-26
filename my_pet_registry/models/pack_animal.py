from .animal import Animal

class PackAnimal(Animal):
    def __init__(self, name, birth_date, species):
        super().__init__(name, birth_date)
        self._species = species

    def make_sound(self):
        sounds = {"Horse": "Neigh", "Donkey": "Hee-haw", "Camel": "Grunt"}
        return sounds.get(self._species, "Unknown sound")
