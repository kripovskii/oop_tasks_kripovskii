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