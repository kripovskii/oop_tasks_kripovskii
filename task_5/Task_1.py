
from abc import abstractmethod, ABC


class ZooPark():

    all_unit_count = 0

    lion_count = 0
    snake_count = 0
    moose_count = 0

    @staticmethod
    def get_count_all_animal():
        print(f"Всего на паре: {ZooPark.all_unit_count} \n Из них {ZooPark.lion_count} Львов,\n {ZooPark.moose_count} оленей,\n {ZooPark.snake_count} Змей")



class Animal(ABC):

    def __init__(self, name, type, age):
        self.name = name
        self.type = type
        self.age = age

        ZooPark.all_unit_count += 1

        if type == "lion":
            ZooPark.lion_count += 1
        elif type == "snake":
            ZooPark.snake_count += 1
        else:
            ZooPark.moose_count += 1

        @abstractmethod
        def get_iam(self):
            print(f"Меня зовут {self.name}, мне {self.age} лет и я {self.type}")

        @abstractmethod
        def get_voice(self):
            print("...")

        @abstractmethod
        def walk(self):
            print("...")

class Lion(Animal):

    def __init__(self, name, type, age):
        super().__init__(name, type, age)

    ZooPark.all_unit_count += 1
    ZooPark.lion_count += 1

    
    def get_iam(self):
        print(f"Меня зовут {self.name}, мне {self.age} лет и я {self.type}")

    
    def get_voice(self):
        print("РРРррррр гхкм")

    
    def walk(self):
        print("Топ-топ-топ")

class Snake(Animal):

    def __init__(self, name, type, age):
        super().__init__(name, type, age)
    
    ZooPark.all_unit_count += 1
    ZooPark.snake_count += 1

    
    def get_iam(self):
        print(f"Меня зовут {self.name}, мне {self.age} лет и я {self.type}")   

    
    def get_voice(self):
        print("Пук-пук-пук")

    
    def walk(self):        
        print("Фить-фить-фить")

class Moose(Animal):

    def __init__(self, name, type, age):
        super().__init__(name, type, age)

    ZooPark.all_unit_count += 1
    ZooPark.moose_count += 1

    
    def get_iam(self):
        print(f"Меня зовут {self.name}, мне {self.age} лет и я {self.type}")

    
    def get_voice(self):
        print("Она мне изменила, ноя ее простил")

    
    def walk(self):
        print("Иду")
        

snake = Snake("nikita", "snake", 18)
snake1 = Snake("sanya", "snake", 18)
snake3 = Snake("danya", "snake", 18)

moose = Moose("evlampiy", "moose", 23)

lion = Lion("oleg", "lion", 20)
lion1 = Lion("kostyan", "lion", 18)


ZooPark.get_count_all_animal()

snake3.get_iam()
snake3.get_voice()
snake3.walk()

moose.get_voice()


