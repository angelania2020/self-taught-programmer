import os
os.path.join("Users", "bob", "st.txt")

#Необходимо закрывать файлы
st=open("st.txt", "w")
st.write("Hello from Python!")
st.close()

#Файл закроется автоматически
with open ("st.txt", "w") as f:
    f.write("Hello from PHP!")
    
with open ("st.txt", "r") as f:
    print(f.read()) #Возвращает итерируемый объект со всеми строками файла.
    
my_list=list()

with open('st.txt', 'w+') as f:
    f.write('Hello from HTML!')
    f.seek(0)  # Important: return to the top of the file before reading, otherwise you'll just read an empty string
    print(f.read())
    f.seek(0)
    my_list.append(f.read())
    
print(my_list)


import csv
with open("st.csv", "w", newline="") as f:
    w=csv.writer(f, delimiter=";")
    w.writerow(["one", "two", "three"])
    w.writerow(["four", "five", "six"])
    
with open("st.csv", "r") as f:
    r=csv.reader(f, delimiter=";")
    for row in r:
        print(";".join(row))
        
with open("st.csv", "r") as f:
    r=csv.reader(f, delimiter=";")
    for row in r:
        print(row)
        
        
#1
from pathlib import Path

data_folder = Path("C:/Users/Angelina/Documents/УЧЁБА В СИЛЛАМЯЭ/!Programmeerimise alused/Мой код/Self-taught programmer")
file_to_open = data_folder / "read.txt"
f = open(file_to_open)
print(f.read())
f.close()



data_folder = Path("C:/Users/Angelina/Documents/УЧЁБА В СИЛЛАМЯЭ/!Programmeerimise alused/Мой код/Self-taught programmer")
file_to_open = data_folder / "read.txt"
print(file_to_open.read_text())



filename = Path("C:/Users/Angelina/Documents/УЧЁБА В СИЛЛАМЯЭ/!Programmeerimise alused/Мой код/Self-taught programmer/read.txt")
print(filename.name)
print(filename.suffix)
print(filename.stem)
print(filename.read_text()) #read file

if not filename.exists():
    print("Oops, file doesn't exist!")
else:
    print("Yay, the file exists!")
    
    
#2
with open ("question.txt", "w+") as f:
    f.write(input("Write something for me:"))
    f.seek(0)
    print(f.read())
if f.closed:
    print("File is closed")
    
    
answer = input("Твой любимый цвет?")
with open("fav_color.txt", "w") as f:
    f.write(answer)


#3
movies=[["Star Wars", "Terminator", "AI"], ["Дурак", "Матильда", "Левиафан"], ["Men in Black", "I am Robot", "Evolution"]]
with open("my_movies.csv", "w", newline="") as f:
    w=csv.writer(f, delimiter=";")
    for movie in movies:
        w.writerow(movie)
           
movies=[["Star Wars", "Terminator", "AI"], ["Дурак", "Матильда", "Левиафан"], ["Men in Black", "I am Robot", "Evolution"]]
with open("my_movies.csv", "w", newline="") as f:
    w=csv.writer(f, delimiter=";")
    w.writerows(movies)



    