class Mlekopitauhie:
    emp_count = 0

    def __init__(self, name, age, klas, pol, eat, idet, slep, herst):
        self.name = name
        self.age = age
        self.klas = klas
        self.pol = pol
        self.eat = eat
        self.idet = idet
        self.slep = slep
        self.herst = herst
        Mlekopitauhie.emp_count += 1

    def output(self):
        print('Имя: {}. Возраст: {}. Вид: {}. Пол: {}. Поел: {}. Идёт: {}. Спит: {}. Шерсть: {}.'.format(self.name, self.age, self.klas, self.pol, self.eat, self.idet, self.slep, self.herst))

anim1 = Mlekopitauhie('Лев', 'Возраст', 'Млекопитающий', 'м','Да','в центр вальера','Да','Длинная')
anim2 = Mlekopitauhie('Лошадь', 'Возраст', 'Непарнокопытный', 'ж','Нет','в левую часть вальера','Нет','Короткая')
class Ptici:
    emp_count = 0

    def __init__(self, name, age, klas, pol, eat, idet, slep, kluv, krilo, gnezdo, egg):
        self.name = name
        self.age = age
        self.klas = klas
        self.pol = pol
        self.eat = eat
        self.idet = idet
        self.slep = slep
        self.kluv = kluv
        self.krilo = krilo
        self.gnezdo = gnezdo
        self.egg = egg
        Ptici.emp_count += 1

    def output1(self):
        print('Имя: {}. Возраст: {}. Вид: {}. Пол: {}. Поел: {}. Полетел: {}. Спит: {}. Размер клюва: {}. Размах крыла: {}. Въёт гнездо: {}. Несёт яица: {}'.format(self.name, self.age, self.klas, self.pol, self.eat, self.idet, self.slep, self.kluv, self.krilo, self.gnezdo, self.egg))

bird1 = Ptici('Синица', 'Возраст', 'Птица', 'м','Да','в центр вальера','Да','10','31','Да','Да')
bird2 = Ptici('Тукан', 'Возраст', 'Птица', 'ж','Нет','в левую часть вальера','Нет','13','23','Да','Нет')


anim1.output()
anim2.output()
bird1.output1()
bird2.output1()