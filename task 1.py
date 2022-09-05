import random
import os

ran = random.randint (1,100) 
count = 0
b = 1

while  b:
    inp = int(input("Введите число от 1 до 100 \n--> "))
    count += 1
    if (ran > inp):
        print ("Ваше число меньше загаданного")   
    elif (ran < inp): 
            print ("Ваше число больше загаданного")
    else: 
        print (f"Вы угадали с {count} попытки") 
        b = 0
os.system("pause")
        
   
          