def check(list, min, max):
    result = 0
    for i in list:
         if i >= min and i < max:
             result += 1
             return result
print(check([1, 3, 5, 6, 8, 2, 4, 6, 234, 7, 57, 345, 7, 234], 1, 15))