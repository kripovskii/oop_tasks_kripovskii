from dataclasses import dataclass
from random import randrange

@dataclass 
class Book:
    name: str
    quantity: int
    quality: str
    price: int


@dataclass
class Clients():
    name: str
    money: int
    item: str

@dataclass
class Shop1():
    book11 = Book("Человек-бензопила", 6, "Новая", 15)
    book12 = Book("Берсерк",2,"Новая", 20)
    book13 = Book("Магическая битва",5,"Новая", 10)

@dataclass
class Shop2():
    book21 = Book("Человек-бензопила", 6, "Подержанное", 8)
    book22 = Book("Берсерк",2,"Подержанное", 13)
    book23 = Book("Магическая битва",5,"Подержанное", 7)

client1 = Clients("Sanya", 50, "")

while(True):
    print("Введите 'help', чтобы открыть список команд")
    command = input()
    if command == "help":
        print("'buy' открыть один из представленных магазинов\n 'mine' заработать денег \n 'wallet' посмотреть баланс \n 'exit' выход \n 'items' посмотреть купленные книги")
    elif command == "buy":
        command2 = input("1. магазин новых книг \n 2. магазин подержанных книг")
        if command2 == "1":
            print(Shop1.book11, "\n",Shop1.book12, "\n",Shop1.book13, "\n")
            
            buy1 = input()
            if buy1 == "1":
                print("Вы купили", Shop1.book11.name, "ваш баланс", client1.money - Shop1.book11.price)
                client1.item += Shop1.book11.name + "\n"

            elif buy1 == "2":
                print("Вы купили", Shop1.book12.name, "ваш баланс", client1.money - Shop1.book12.price)
                client1.item+= Shop1.book12.name + "\n"
            else:
                print("Вы купили", Shop1.book13.name, "ваш баланс", client1.money - Shop1.book13.price)
                client1.item += Shop1.book13.name + "\n"

        elif command2 == "2":
            print(Shop2.book21, "\n",Shop2.book22, "\n",Shop2.book23, "\n")
            
            buy2 = input()
            if buy2 == "1":
                print("Вы купили", Shop2.book11.name, "ваш баланс", client1.money - Shop2.book21.price)
                client1.item += Shop2.book21.name + "\n"
            elif buy2 == "2":
                print("Вы купили", Shop2.book12.name, "ваш баланс", client1.money - Shop2.book22.price)
                client1.item += Shop2.book22.name + "\n"
            else:
                print("Вы купили", Shop2.book13.name, "ваш баланс", client1.money - Shop2.book23.price)
                client1.item += Shop2.book23.name + "\n"
    elif command == "mine":
        print("введите правильный ответ\n")
        for i in range(1, 6):
            x = randrange(1, 9)
            y = randrange(1, 9)
            print(x," * ", y, " =")
            result = int(input())

            if result == (x*y):
                client1.money += randrange(1,10)
                print("true: ваш баланс ", client1.money)
            else:
                print("falce")

    elif command == "wallet":
        print("ваш баланс", client1.money)

    elif command == "items":
        print(client1.item)

    elif command == "exit":
        break
    
    