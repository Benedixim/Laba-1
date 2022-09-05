import random
import os


size = int(input("Введите размер массива \n--> "))

from random import randint
my_list=[randint(0,5) for i in range(size)]
my_copy = []
   
print (my_list) 



for i in my_list:
    if my_list.count(i) == 1: my_copy.append(i)    

if not my_copy: print("Уникальных чисел нет")
else: print ("Уникальные числа:",*my_copy) 
        

sum = 0

if my_list.count(0)<2: print("В списке не хватает нулей")
else:
    first = my_list.index(0)
    print(f"Первое нуловое значение находится на {first}-ом месте в списке")

    my_list.reverse()
    last = size - my_list.index(0) - 1
    print(f"Второе нуловое значение находится на {last}-ом месте в списке")
    my_list.reverse()

    while first < last:
        sum += my_list[first]
        first += 1

    print ("Сумма между первым и последним нулем составляет = ", sum)

os.system("pause")