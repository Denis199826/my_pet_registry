# Базовый класс Animal
class Animal:
    def __init__(self, name: str, age: int):
        self._name = name     # Инкапсуляция поля _name
        self._age = age       # Инкапсуляция поля _age

    def make_sound(self):
        raise NotImplementedError("This method should be overridden in subclasses")

    def info(self):
        """Возвращает информацию о животном."""
        return f"Name: {self._name}, Age: {self._age}"


# Подкласс для домашних животных
class Pet(Animal):
    def __init__(self, name: str, age: int, species: str):
        super().__init__(name, age)
        self._species = species  # Инкапсуляция вида животного

    def info(self):
        """Дополнение информации о виде животного."""
        return f"{super().info()}, Species: {self._species}"


# Подкласс для вьючных животных
class PackAnimal(Animal):
    def __init__(self, name: str, age: int, species: str):
        super().__init__(name, age)
        self._species = species  # Инкапсуляция вида животного

    def info(self):
        """Дополнение информации о виде животного."""
        return f"{super().info()}, Species: {self._species}"


# Конкретные классы для домашних животных
class Dog(Pet):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, species="Dog")

    def make_sound(self):
        return "Woof"


class Cat(Pet):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, species="Cat")

    def make_sound(self):
        return "Meow"


class Hamster(Pet):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, species="Hamster")

    def make_sound(self):
        return "Squeak"


# Конкретные классы для вьючных животных
class Horse(PackAnimal):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, species="Horse")

    def make_sound(self):
        return "Neigh"


class Camel(PackAnimal):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, species="Camel")

    def make_sound(self):
        return "Grunt"


class Donkey(PackAnimal):
    def __init__(self, name: str, age: int):
        super().__init__(name, age, species="Donkey")

    def make_sound(self):
        return "Hee-haw"


if __name__ == "__main__":
    # Создание объектов домашних животных
    dog = Dog("Buddy", 4)
    cat = Cat("Whiskers", 2)
    hamster = Hamster("Nibbles", 1)

    # Создание объектов вьючных животных
    horse = Horse("Spirit", 5)
    camel = Camel("Camo", 6)
    donkey = Donkey("Eeyore", 3)

    # Вывод информации о животных
    animals = [dog, cat, hamster, horse, camel, donkey]
    for animal in animals:
        print(animal.info())
        print(f"Sound: {animal.make_sound()}")
        print("-" * 20)
