class Shape():
    def __init__(self,name,color,ugli):
        self.name = name
        self.color = color
        self.ugli = ugli
    def information(self,):
        print(f"Имя = {self.name}, Цвет = {self.color}, Количество углов = {self.ugli}")
shape = Shape("Shape", "синий", 4)
shape.information()
print('________________________________')
class crug(Shape):
    def __init__(self,name,color,ugli, radius):
        super().__init__(name,color,ugli)
        self.constant = 3.14
        self.radius = radius
    def perimeter(self,):
        P = 2 * self.constant *self.radius
        print(P)
    def __square(self,):
        s = self.constant * self.radius**2
        return s
    def volume(self, hight):
        v = self.__square() * hight
        print(v)
crug = crug('Круг', 'Жёлтый', 0, 16)
crug.information()
crug.perimeter()
print(crug._crug__square())
crug.volume(16)
print('1.Периметр, 2.Площадь, 3.Объём')
print('________________________________')
class triugolnic(Shape):
    def __init__(self, name, color, ugli):
        super().__init__(name, color, ugli)
        self.__base = 8
        self.__hight = 10
    def get(self):
        print(f'Основание = {self.__base}, Высота = {self.__hight}')
    def set(self,new_base, new_hight):
        self.__base = new_base
        self.__hight = new_hight

    def perimeter(self,a,b,c):
        p = a + b + c
        print(p)
        
    
    def __square(self):
        s = 1/2 * self.__base * self.__hight
        return s
    
    def volume(self, hight_of_prisma):
        p = self.__square()
        v = p * hight_of_prisma
        print(v)

triugolnic = triugolnic('Трeугольник','зелёный',3,)
triugolnic.information()
triugolnic.perimeter(5,5,5)
print(triugolnic._triugolnic__square())
triugolnic.volume(10)
print('1.Периметр, 2.Площадь, 3.Объём')



