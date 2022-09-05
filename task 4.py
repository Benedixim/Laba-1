import os

st = input("Введите cтроку \n--> ")
my_dict = {}

for i in st:
   my_dict[int(i)] = st.count(i)

print("Словарь: ", my_dict)
os.system("pause")