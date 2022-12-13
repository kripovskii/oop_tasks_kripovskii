class Filial():
    filial_holder = []
    filials = 0

    def __init__(self, name, worker, god_doh, yearly_spent):
        self.name = name
        self.worker = worker
        self.god_doh = god_doh
        self.yearly_spent = yearly_spent
        Filial.filials += 1
        Filial.filial_holder.append(self)

    def increase_income(self):
        self.god_doh += 1000
        print(f"Годовой доход = {self.god_doh} (больше на 1000)")

    def decrease_income(self):
        self.god_doh -= 1000
        print(f"Годовой доход = {self.god_doh} (меньше на 1000)")

    def increase_spent(self):
        self.yearly_spent += 1000
        print(f"Годовые расходы = {self.yearly_spent} (больше на 1000)")

    def decrease_spent(self):
        self.yearly_spent -= 1000
        print(f"Годовые расходы = {self.yearly_spent} (меньше на 1000)")

    def __pribil(self):
        self.pribil = self.god_doh - self.yearly_spent
        return self.pribil

    def self_present(self):
        print(
            f"Привет, мы {self.name}! У нас {self.worker} работников, наш ежегодный доход {self.god_doh} и наши ежегодные расходы {self.yearly_spent}!")

    @classmethod
    def count_filials(self):
        print(f"У компании всего {Filial.filials} филиала(ов)")

    @classmethod
    def self_present_all(self):
        for i in range(Filial.filials):
            Filial.filial_holder[i].self_present()

    @classmethod
    def full_income(self):
        allincome = 0
        for i in range(Filial.filials):
            allincome += Filial.filial_holder[i].god_doh
        print(f"Общий доход: {allincome}")

    @classmethod
    def full_spent(self):
        allspent = 0
        for i in range(Filial.filials):
            allspent += Filial.filial_holder[i].yearly_spent
        print(f"Общие расходы: {allspent}")

    @classmethod
    def full_prib(self):
        allprib = 0
        for i in range(Filial.filials):
            allprib += Filial.filial_holder[i].__pribil()
        print(f"Общая прибыль: {allprib}")
        if allprib < 0:
            print("Бизнес убыточный")


filial1 = Filial("Филиал1", 30, 2000, 3000)
filial1.increase_income()
filial1.decrease_income()
filial1.increase_spent()
filial1.decrease_spent()
filial1.self_present()

filial2 = Filial("Филиал2", 45, 5000, 6000)
filial3 = Filial("Филиал3", 70, 15000, 14000)

print("\n")
Filial.count_filials()
Filial.self_present_all()
Filial.full_income()
Filial.full_spent()
Filial.full_prib()
