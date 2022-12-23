from random import randint

class Chicken():
    def __init__(self):
        self.eggs = randint(1,101)
        self.name = "Курица"
    def i_chicken(self):
        print(f'Я {self.name}.', end='')
    def eggs_count(self):
        print(f' Я снесла {self.eggs} яиц.')
chicken = Chicken()

class Russian_chicken(Chicken):
    def __init__(self,):
        super().__init__()
        self.eggs = 6
        self.country = 'Россия'
    def i_chicken(self):
        print(f'Я {self.name}.', f'Страна: {self.country}. ', end='')
    def eggs_count(self):
        print(f'Я снесла {self.eggs} яиц.')
russian_chicken = Russian_chicken()

class Belarusian_chicken(Chicken):
    def __init__(self,):
        super().__init__()
        self.eggs = 30
        self.country = 'Белорусия'
    def i_chicken(self):
        print(f'Я {self.name}.', f'Страна: {self.country}. ', end='')
    def eggs_count(self):
        print(f'Я снесла {self.eggs} яиц.')
belarusian_chicken = Belarusian_chicken()

class Moldovan_chicken(Chicken):
    def __init__(self,):
        super().__init__()
        self.eggs = 73
        self.country = 'Молдавия'
    def i_chicken(self):
        print(f'Я {self.name}.', f'Страна: {self.country}. ', end='')
    def eggs_count(self):
        print(f'Я снесла {self.eggs} яиц.')
moldovan_chicken = Moldovan_chicken()
if __name__ == '__main__':
    chicken.i_chicken(), chicken.eggs_count()
    russian_chicken.i_chicken(), russian_chicken.eggs_count()
    belarusian_chicken.i_chicken(), belarusian_chicken.eggs_count()
    moldovan_chicken.i_chicken(), moldovan_chicken.eggs_count()



