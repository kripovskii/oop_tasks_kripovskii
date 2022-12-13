from zadaniech import Russian_chicken, Belarusian_chicken, Moldovan_chicken

class Poultry_farm():
    def __russian_chicken(self,):
        self.rus_chick = Russian_chicken()
        return self.rus_chick


    def __belarusian_chicken(self,):
        self.bel_chick = Belarusian_chicken()
        return self.bel_chick

    def __moldovan_chicken(self,):
        self.mol_chick = Moldovan_chicken()
        return self.mol_chick


    def __init__(self):
        self.__count_of_russian_chicken = 25
        self.__count_of_belarusian_chicken = 100
        self.__count_of_moldova_chicken = 50

    def __count_of_all_chicken(self,):
        return self.__count_of_russian_chicken + self.__count_of_belarusian_chicken + self.__count_of_moldova_chicken

    def __count_of_all_eggs(self,):
        return self.__count_of_russian_chicken * self.__russian_chicken().eggs + self.__count_of_belarusian_chicken * self.__belarusian_chicken().eggs + self.__count_of_moldova_chicken * self.__moldovan_chicken().eggs

    def get_count_of_russian_chicken(self):
        return self.__count_of_russian_chicken

    def get_count_of_belarusian_chicken(self):
        return self.__count_of_belarusian_chicken

    def get_count_of_moldova_chicken(self):
        return self.__count_of_moldova_chicken

    def get_count_of_all_chicken(self):
        return self.__count_of_all_chicken()
    
    def get_count_of_all_eggs(self):
        return self.__count_of_all_eggs()

p = Poultry_farm()
print(p.get_count_of_all_eggs())