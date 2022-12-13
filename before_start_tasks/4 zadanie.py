number = str(input('Месяц: '))
if number in ('Январь', 'Февраль', 'Декабрь'):
    print('Зима')
elif number in ('Март', 'Апрель', 'Май'):
    print('Весна')
elif number in ('Июнь', 'Июль', 'Август'):
    print('Лето')
elif number in ('Сентябрь', 'Октябрь', 'Ноябрь'):
    print('Осень')
else:
    print('Нет')