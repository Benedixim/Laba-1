import os

st = input("Введите cтроку \n--> ")
ls = st.split(sep=" ")

count_n = 0 #нечетное
count_c = 0 #четное

for i in ls:
    if len(i) % 2 == 0:
        count_c +=1
    else:
        count_n += 1

print ("Количество слов чётной длины =", count_c)   #четное
print ("Количество слов нечётной длины =", count_n) #нечетное

os.system("pause")