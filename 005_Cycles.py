name="Ted"
for character in name:
    print(character)
    

shows=["Breaking Bad", "X-Files", "Fargo"]
for show in shows:
    print(show)
    
    
coms=("Big Bang Theory", "Friends", "Pushing Daisies")
for show in coms:
    print(show)
    

people={"Jim Parsons":"Big Bang Theory",
        "Bryan Cranston":"Breaking Bad",
        "Lee Pace":"Pushing Daisies"
}
for character in people:
    print(character)
    
    
tv=["Breaking Bad", "X-Files", "Fargo"]

i=0
for show in tv:
    new=tv[i]
    new=new.upper()
    tv[i]=new
    i+=1
print(tv)

for i, show in enumerate(tv):
    new=tv[i]
    new=new.upper()
    tv[i]=new
print(tv)


tv=["Breaking Bad", "X-Files", "Fargo"]
coms=["Big Bang Theory", "Friends", "Pushing Daisies"]
all_shows=[]

for show in tv:
    show=show.upper()
    all_shows.append(show)

for show in coms:
    show=show.upper()
    all_shows.append(show)

print(all_shows)


for i in range(1,11):
    print(i) #1-10
    
x=10
while x>0:
    print('{}'.format(x))
    x-=1
print("С Новым годом!")


while True:
    print('Hello, world!')
    
    
for i in range(0,100):
    print(i)
    

for i in range(0,100):
    print(i)
    break


qs=["What is your name?", "Your favourite colour?", "What are you doing?"]
n=0
while True:
    print("To exit press X")
    a=input(qs[n])
    if a=="X":
        break
    n=(n+1)%3
    

for i in range(1,6):
    if i==3:
        continue
    print(i)
    
    
i=1
while i<=5:
    if i==3:
        i+=1
        continue
    print(i)
    i+=1
    
    
for i in range(1,3):
    print(i) 
    for letter in ["a", "b", "c"]:
        print(letter)
        
    
list1=[1,2,3,4]
list2=[5,6,7,8]
added=[]
for i in list1:
    for j in list2:
        added.append(i+j)
print(added)
#[6, 7, 8, 9, 7, 8, 9, 10, 8, 9, 10, 11, 9, 10, 11, 12]


list1=[1,2,3,4]
list2=[5,6,7,8]
added=[]
n=0
for i in list1:
    j=list2[n]
    added.append(i+j)
    n+=1
print(added)
#[6, 8, 10, 12]


while input("д или н?")!="н":
    for i in range(1,6):
        print(i)
        
#1
list=["Ходячие мертвецы", "Красавцы", "Клан Сопрано", "Дневники вампира"]
for show in list:
    print(show)


#2
for i in range(25,51):
    print(i)


#3
list=["Ходячие мертвецы", "Красавцы", "Клан Сопрано", "Дневники вампира"]
for i, show in enumerate(list):
    print(i,show)


#4
list=[5, 66, 324, 999, 76]
while True:
    guess=input("Отгадайте число или введите \"X\" для выхода.")
    if guess=="X":
        break
    try:
        if int(guess) in list:
            print("Вы отгадали!")
        else:
            print("Вы не отгадали!")
    except ValueError:
        print("Ошибка.")
    

numbers = [11, 32, 33, 15, 1]
while True:
    answer = input("Угадайте число или введите Х для выхода.")
    if answer == "Х":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("пожалуйста, введите число или Х для выхода.")
    if answer in numbers:
        print("Вы угадали!")
    else:
        print("Неправильно!")



#5
list1=[8,19,148,4]
list2=[9,1,33,83]
list3=[]
for i in list1:
    for j in list2:
        list3.append(i*j)
print(list3)