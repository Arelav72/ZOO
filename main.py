class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def eat(self):
        return "Животное ест"

class Bird(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)


    def make_sound(self):
        return f"{self.name} поет ЧикЧирик"

class Mammal(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)


    def make_sound(self):
        return f"{self.name} рычит РЫЫЫ"

class Reptile(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)


    def make_sound(self):
        return f"{self.name} рычит Ррррр"

def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())

class Zoo:
    def __init__(self):
        self.animals = []
        self.people = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_piple(self, piple):
        self.people.append(piple)

    def list_animals(self):
        for animal in self.animals:
            print(f'{animal.name}, the {animal.__class__.__name__}')

    def list_piples(self):
        for piple in self.people:
            print(f'{piple.name}, the {piple.__class__.__name__}')

class Piple:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info_piple(self):
        print(f"{self.name} - возраст {self.age}")

class ZooKeeper(Piple):
    def __init__(self, name, age):
        super().__init__(name, age)

    def feed_animal(self):
        print(f"{self.name} кормит")

class Veterinarian(Piple):
    def __init__(self, name, age):
        super().__init__(name, age)

    def heal_animal(self):
        print(f"{self.name} лечит")

# Демонстрация полиморфизма
animals = [Bird("Голубка", 2 ), Mammal("Шарик ", 5), Reptile("Гена", 4)]
animal_sound(animals)

# Создание и использование объекта Zoo

zoo = Zoo()
zoo.add_animal(Bird("Гоша", 3))
zoo.add_animal(Mammal("Шарик ", 5))
zoo.add_animal(Reptile("Гена", 4))
zoo.add_piple(ZooKeeper("Иван Иванович", 55))
zoo.add_piple(Veterinarian("Петр Петрович", 62))
zoo.list_animals()

# Сохранение информации о зоопарке в файл
def save_zoo_state(zoo, filename):
    with open(filename, "w") as file:
        for animal in zoo.animals:
            file.write(f'{animal.name}, {animal.age},  {animal.__class__.__name__}\n')

# Загрузка информации о зоопарке из файла
def load_zoo_state(zoo, filename):
    with open(filename, "r") as file:
        for line in file:
            name, age, type_ = line.strip().split(", ")
            if type_ == "Bird":
                zoo.add_animal(Bird(name, int(age)))
            elif type_ == "Mammal":
                zoo.add_animal(Mammal(name, int(age)))
            elif type_ == "Reptile":
                zoo.add_animal(Reptile(name, int(age)))


# Сохранение информации о зоопарке в файл
save_zoo_state(zoo, "zoo_state.txt")
load_zoo_state(zoo, "zoo_state.txt")

# Загрузка информации о зоопарке из файла
zoo.list_animals()  # должен вывести список животных, включая загруженные
zoo.list_piples()  # должен вывести список сотрудников, включая загруженные