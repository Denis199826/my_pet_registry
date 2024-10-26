

class Animal:
    def __init__(self, name, birth_date):
        self._name = name
        self._birth_date = birth_date
        self._commands = []

    def get_name(self):
        return self._name

    def get_birth_date(self):
        return self._birth_date

    def get_commands(self):
        return self._commands

    def add_command(self, command):
        self._commands.append(command)

    def make_sound(self):
        pass  # Placeholder for subclass-specific sound


class Pet(Animal):
    def __init__(self, name, birth_date, species):
        super().__init__(name, birth_date)
        self._species = species

    def make_sound(self):
        sounds = {"Dog": "Bark", "Cat": "Meow", "Hamster": "Squeak"}
        return sounds.get(self._species, "Unknown sound")


class PackAnimal(Animal):
    def __init__(self, name, birth_date, species):
        super().__init__(name, birth_date)
        self._species = species

    def make_sound(self):
        sounds = {"Horse": "Neigh", "Donkey": "Hee-haw", "Camel": "Grunt"}
        return sounds.get(self._species, "Unknown sound")
