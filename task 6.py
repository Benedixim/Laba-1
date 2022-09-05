import random
import os


size = int(input("Введите размер кортежа \n--> "))
my_tuple = tuple([random.randint(0,5) for i in range(size)])
print ("Кортеж - ", my_tuple)


print ("Количество нулей в кортеже = ",my_tuple.count(0))


os.system("pause")