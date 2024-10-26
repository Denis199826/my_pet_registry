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


# Реестр для хранения всех животных
class PetRegistry:
    def __init__(self):
        self.animals = []  # Список для хранения всех животных

    def add_animal(self, animal):
        """Добавляет животное в реестр."""
        self.animals.append(animal)
        print(f"{animal.get_name()} has been added to the registry.")

    def list_animals(self):
        """Выводит всех животных в реестре."""
        if not self.animals:
            print("No animals in the registry.")
        else:
            print("Animals in the registry:")
            for idx, animal in enumerate(self.animals, start=1):
                print(f"{idx}. {animal.get_name()} ({animal.__class__.__name__}), Born on: {animal.get_birth_date()}")

    def show_commands(self, animal_name):
        animal = self._find_animal(animal_name)
        if animal:
            print(f"{animal_name} can perform these commands: {', '.join(animal.get_commands()) or 'No commands'}")
        else:
            print(f"No animal named {animal_name} found.")

    def train_new_command(self, animal_name, command):
        animal = self._find_animal(animal_name)
        if animal:
            animal.add_command(command)
            print(f"New command '{command}' trained to {animal_name}.")
        else:
            print(f"No animal named {animal_name} found.")

    def _find_animal(self, animal_name):
        for animal in self.animals:
            if animal.get_name() == animal_name:
                return animal
        return None

    def menu(self):
        while True:
            print("\nPet Registry Menu:")
            print("1. Add new animal")
            print("2. List animals")
            print("3. Show commands for an animal")
            print("4. Train animal to new command")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self._add_new_animal()
            elif choice == '2':
                self.list_animals()
            elif choice == '3':
                animal_name = input("Enter the animal's name: ")
                self.show_commands(animal_name)
            elif choice == '4':
                animal_name = input("Enter the animal's name: ")
                command = input(f"Enter the new command for {animal_name}: ")
                self.train_new_command(animal_name, command)
            elif choice == '5':
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please select again.")

    def _add_new_animal(self):
        name = input("Enter animal's name: ")
        birth_date = input("Enter animal's birth date (YYYY-MM-DD): ")
        animal_type = input("Enter animal type (Pet or PackAnimal): ").capitalize()

        if animal_type == "Pet":
            species = input("Enter species (Dog, Cat, Hamster): ").capitalize()
            animal = Pet(name, birth_date, species)
        elif animal_type == "Packanimal":
            species = input("Enter species (Horse, Camel, Donkey): ").capitalize()
            animal = PackAnimal(name, birth_date, species)
        else:
            print("Unsupported animal type.")
            return

        self.add_animal(animal)  # Добавление животного в реестр
        print(f"{animal_type} named {name} has been added.")
