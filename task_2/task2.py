class Person():
    def __init__(self, name):
        self.name = name
        self.health = 1
        self.weapon = "без оружия"
        self.phisical_hit = 1
        self.fire_hit = 1
        self.chemical_hit = 1
        self.electro_hit = 1
        self.psy_hit = 1
        self.cold_hit = 1
        self.energy_hit = 1
        self.emi_hit = 1
        self.radiation_hit = 1
        self.armor = "без брони"
        self.phisical_resist = 1
        self.fire_resist = 1
        self.chemical_resist = 1
        self.electro_resist = 1
        self.psy_resist = 1
        self.cold_resist = 1
        self.energy_resist = 1
        self.emi_resist = 1
        self.radiation_resist = 1
    def check_health(self):
        if self.health <= 0:
            print("Персонаж по имени " + str(self.name) + " погиб")
    def atack(self, enemy):
        enemy.health -= self.phisical_hit * (1 - enemy.phisical_resist) + self.fire_hit * (1 - enemy.fire_resist) + self.chemical_hit * (1 - enemy.chemical_resist) \
                        + self.phisical_hit * (1 - enemy.phisical_resist) + self.electro_hit * (1 - enemy.electro_resist) + self.psy_hit * (1 - enemy.psy_resist) \
                        + self.cold_hit * (1 - enemy.cold_resist) + self.energy_hit * (1 - enemy.energy_resist) + self.emi_hit * (1 - enemy.emi_resist) + self.radiation_hit * (1 - enemy.radiation_resist)
        if enemy.health <= 0:
            print("Персонаж " + str(enemy.name) + " был убит персонажем " + str(self.name))
        else:
            print("Персонаж " + str(enemy.name) + " получил урон от персонажа " + str(self.name) + " на " + str(self.phisical_hit * (1 - enemy.phisical_resist) + self.fire_hit * (1 - enemy.fire_resist) + self.chemical_hit * (1 - enemy.chemical_resist) \
                        + self.phisical_hit * (1 - enemy.phisical_resist) + self.electro_hit * (1 - enemy.electro_resist) + self.psy_hit * (1 - enemy.psy_resist) \
                        + self.cold_hit * (1 - enemy.cold_resist) + self.energy_hit * (1 - enemy.energy_resist) + self.emi_hit * (1 - enemy.emi_resist) + self.radiation_hit * (1 - enemy.radiation_resist)) + " единиц")
        enemy.check_health()
    def take_weapon(self, weapon):
        self.weapon = weapon.name
        self.phisical_hit = weapon.phisical_hit
        self.fire_hit = weapon.fire_hit
        self.chemical_hit = weapon.chemical_hit
        self.electro_hit = weapon.electro_hit
        self.psy_hit = weapon.psy_hit
        self.cold_hit = weapon.cold_hit
        self.energy_hit = weapon.energy_hit
        self.emi_hit = weapon.emi_hit
        self.radiation_hit = weapon.radiation_hit
    def take_armor(self, armor):
        self.armor += armor.name
        self.phisical_resist += armor.phisical_resist
        self.fire_resist += armor.fire_resist
        self.chemical_resist += armor.chemical_resist
        self.electro_resist += armor.electro_resist
        self.psy_resist += armor.psy_resist
        self.cold_resist += armor.cold_resist
        self.energy_resist += armor.energy_resist
        self.emi_resist += armor.emi_resist
        self.radiation_resist = armor.radiation_resist

weapons = []
armors = []

class Weapon():
    def __init__(self, name, phisical_hit, fire_hit, chemical_hit, electro_hit, psy_hit, cold_hit, energy_hit, emi_hit, radiation_hit):
        self.name = name
        self.phisical_hit = phisical_hit
        self.fire_hit = fire_hit
        self.chemical_hit = chemical_hit
        self.electro_hit = electro_hit
        self.psy_hit = psy_hit
        self.cold_hit = cold_hit
        self.energy_hit = energy_hit
        self.emi_hit = emi_hit
        self.radiation_hit = radiation_hit
        weapons.append(self)

class Armor():
    def __init__(self, name, phisical_resist, fire_resist, chemical_resist, electro_resist, psy_resist, cold_resist, energy_resist, emi_resist, radiation_resist):
        self.name = name
        self.phisical_resist = phisical_resist
        self.fire_resist = fire_resist
        self.chemical_resist = chemical_resist
        self.electro_resist = electro_resist
        self.psy_resist = psy_resist
        self.cold_resist = cold_resist
        self.energy_resist = energy_resist
        self.emi_resist = emi_resist
        self.radiation_resist = radiation_resist
        armors.append(self)

class Human(Person):
    def __init__(self, name):
        super().__init__(name)
        self.health = 100
        self.phisical_hit = 10
        self.fire_hit = 0
        self.chemical_hit = 0
        self.electro_hit = 0
        self.psy_hit = 0
        self.cold_hit = 0
        self.energy_hit = 0
        self.emi_hit = 0
        self.radiation_hit = 0
        self.phisical_resist = 0.10
        self.fire_resist = 0.05
        self.chemical_resist = 0.05
        self.electro_resist = 0.05
        self.psy_resist = 0.20
        self.cold_resist = 0.05
        self.energy_resist = 0.05
        self.emi_resist = 0.99
        self.radiation_resist = 0.05
    def healthing(self):
        self.health += 33


class Robot(Person):
    def __init__(self, name):
        super().__init__(name)
        self.health = 100
        self.phisical_hit = 30
        self.fire_hit = 0
        self.chemical_hit = 0
        self.electro_hit = 0
        self.psy_hit = 0
        self.cold_hit = 0
        self.energy_hit = 0
        self.emi_hit = 0
        self.radiation_hit = 0
        self.phisical_resist = 0.40
        self.fire_resist = 0.25
        self.chemical_resist = 1
        self.electro_resist = 0.20
        self.psy_resist = 1
        self.cold_resist = 0.20
        self.energy_resist = 0.30
        self.emi_resist = 0
        self.radiation_resist = 0.95
    def hot_reactor(self):
        self.health -= 40
        self.check_health()
        self.fire_hit = 5
        self.electro_hit = 5
        self.energy_hit = 5
        self.radiation_hit = 40
        self.phisical_resist = 0.20
        self.fire_resist = 0.01
        self.electro_resist = 0.01
        self.cold_resist = 1
        self.energy_resist = 0.01
        self.radiation_resist = 0.01

class Mutant(Person):
    def __init__(self, name):
        super().__init__(name)
        self.health = 80
        self.phisical_hit = 15
        self.fire_hit = 0
        self.chemical_hit = 2
        self.electro_hit = 0
        self.psy_hit = 0
        self.cold_hit = 0
        self.energy_hit = 0
        self.emi_hit = 0
        self.radiation_hit = 5
        self.phisical_resist = 0.08
        self.fire_resist = 0.02
        self.chemical_resist = 0.60
        self.electro_resist = 0.02
        self.psy_resist = 0.70
        self.cold_resist = 0.02
        self.energy_resist = 0.02
        self.emi_resist = 0.99
        self.radiation_resist = 1.5
    def mutation(self):
        self.health += 20
        self.phisical_hit = 30
        self.chemical_hit = 5
        self.radiation_hit = 15
        self.phisical_resist = 0.20
        self.fire_resist = 0.20
        self.chemical_resist = 0.01
        self.electro_resist = 0.20
        self.psy_resist = 0.20
        self.cold_resist = 0.20
        self.energy_resist = 0.20
        self.emi_resist = 0.99
        self.radiation_resist = 0.02

pistol = Weapon("пистолет", 20, 0, 0, 0, 0, 0, 0, 0, 0)
emi_granade = Weapon("ЭМИ граната", 0, 0, 0, 0, 50, 0, 0, 100, 0)
rad_gun = Weapon("Радиокативная пушка", 0, 0, 0, 0, 0, 0, 0, 0, 100)
print(weapons)
h1 = Human("Чел")
r1 = Robot("1010101011")
m1 = Mutant("Супермутант")
r1.take_weapon(pistol)
print(h1.weapon)
m1.take_weapon(emi_granade)
h1.take_weapon(rad_gun)
r1.atack(h1)
m1.atack(r1)
h1.healthing()
h1.atack(m1)