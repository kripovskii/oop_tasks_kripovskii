class Gun:
    def __init__(self, name):
        self.name = name
        self.health = 1000
        self.magazine = 10
        self.tochnost = 3.00
        self.dalnost = 2500
        self.stvol = 0
        while self.magazine < 1:
            if self.stvol == 0:
                self.magazine -= 1
    def pif(self):
        if self.magazine == 0:
            print("Нужно перезарядится")
        else:
            self.magazine -= 1
            self.health -= 1
            self.tochnost -= 0.0001
            self.dalnost -= 0.1
            print("Вы произвели выстрел")
    def razradka(self):
        self.magazine = 0
        self.stvol = 0
        print("Вы разрядили оружие")
    def zaradka(self):
        self.magazine = 10
        print("Вы зарядили оружие")
    def remont(self):
        self.health = 1000
        self.tochnost = 3.00
        self.dalnost - 2500
        print("Вы отремонтировали оружие")
M1A = Gun("M1A")
for i in range (0, 31):
    M1A.pif()
print(M1A.health)

class Cat:
    def __init__(self, name, color, age):
       self.name = name
       self.color = color
       self.age = age
       self.hungry = 40
       self.agresive = 10
       self.stamina = 100
       self.loud = 2
       self.lazy = 100
    def mau(self):
        print("Мяу")
        if self.hungry > 70:
            self.loud = 10
            print("МЯУ")
    def shh(self):
        print("Шипение")
        self.agresive += 20
    def food(self):
        self.hungry -= 30
        self.loud = 2
        "Вы дали коту корм".upper()
    def play(self):
        self.stamina -= 40
        self.hungry += 10
        print("Вы поиграли с котом")
cat = Cat("Вася", "Чёрно-беллый", 3)
print(cat.name)
cat.play()
cat.play()
cat.play()
cat.play()
cat.mau()
cat.food()
cat.food()
print("Голод:",cat.hungry)