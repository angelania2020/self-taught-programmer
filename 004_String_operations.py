'''line one
   line two
   line three
'''

author='Kafka'
print(author[0])
print(author[1])
print(author[2])
print(author[3])
print(author[4])
#print(author[5]) #IndexError: string index out of range
print(author[-1])
print(author[-2])
print(author[-3])
print(author[-4])
print(author[-5])
#print(author[-6]) #IndexError: string index out of range

#Строки неизменяемы
ff='F. Fitzgerald'
ff='F. Scott Fitzgerald'
print(ff)

#Конкатенация
print('cat'+'in'+'the'+'hat') #catinthehat
print('cat'+' in'+' the'+' hat') #cat in the hat

#Умножение строк
print('Sawyer'*3) #SawyerSawyerSawyer

#Изменение регистра
print('Истина где-то рядом...'.upper()) #ИСТИНА ГДЕ-ТО РЯДОМ...
print('ТАК БУДЕТ ПРОДОЛЖАТЬСЯ.'.lower()) #так будет продолжаться.
print('троглодиты...'.capitalize()) #Троглодиты...

#Method format
'William {}'.format('Faulkner')

last='Faulkner'
'William {}'.format(last)

author="William Faulkner"
year_born="1897"
"{} was born in {}.".format(author, year_born)

n1=input("Enter a noun: ")
v=input("Enter a verb: ")
adj=input("Enter an adjective: ")
n2=input("Enter a noun: ")
r="""As usual, {} {} {} {}
""".format(n1,
           v,
           adj,
           n2)
print(r)


"Я прыгнул через голову.Это целых 2 метра!".split(".")


first_three="abc"
result="+".join(first_three)
result #'a+b+c'


words=["Рыжая", "лисица", "сделала", "кувырок", "через", "голову", "."]
one="".join(words)
print(one) #Рыжаялисицасделалакувырокчерезголову.


words=["Рыжая", "лисица", "сделала", "кувырок", "через", "голову", "."]
one=" ".join(words)
print(one) #Рыжая лисица сделала кувырок через голову .


s="     Moscow         "
s=s.strip()
print(s)


equ="All animals are equal."
equ=equ.replace("a", "@")
print(equ) #All @nim@ls @re equ@l.


print("animals".index("n")) #1
print("animals".index("a")) #0


try:
    "animals".index("o")
except:
    print("Not found.")


"Cat" in "Cat in the hat."

"Mouse" in "Cat in the hat."

"Potter" not in "Harry"


"She said "Definitely."" #SyntaxError: invalid syntax
"She said \"Definitely.\"" #'She said "Definitely."'
'She said \"Definitely.\"' #'She said "Definitely."'
'She said "Definitely."' #'She said "Definitely."'
"She said 'Definitely.'" #"She said 'Definitely.'"


# \n - перенос строки
print("line1\nline2\nline3")

#Извлечение среза
fict = ["Tolstoy", "Dick", "Orwell", "Austin", "Meyer"]
print(fict[0:3]) #['Tolstoy', 'Dick', 'Orwell']

ivan="""Петр Иванович успокоился и с интересом стал
расспрашивать подробности о кончине Ивана Ильича."""
print(ivan[0:24])
print(ivan[:24])
print(ivan[24:93])
print(ivan[24:])
print(ivan[:])
print(len(ivan))

#1
author="Чехов"
print(author[0])
print(author[1])
print(author[2])
print(author[3])
print(author[4])

for character in author:
    print(character)

#2
string1=input("Enter a noun: ")
string2=input("Enter a noun: ")
print("Вчера я написал {}. Вчера я ходил в {}!".format(string1,string2))

#3
wrong="олдос Хаксли родился в 1894 году."
wrong.capitalize() #'Олдос хаксли родился в 1894 году.'
x = "олдос Хаксли родился в 1894 году. он родился в Великобритании.".title()
wrong.title() #'Олдос Хаксли Родился В 1894 Году.'


wrong="олдос Хаксли родился в 1894 году."
right = wrong[0].capitalize() + wrong[1:] Олдос Хаксли родился в 1894 году.
print(right)

#4
a="Где это? Кто это? Когда это?".split("?")
b=[(phrase+"?").strip() for phrase in a]
c=b.pop()
print(b)


#5
list=["Рыжая", "лиса", "перепрыгнула", "через", "низкий", "забор", "."]
sentence1=" ".join(list)
sentence2=sentence[0:-2]+"."
print(sentence2)


#6
line="Ребёнок – зеркало поступков родителей."
print(line.replace("о", "0")) #"о" должна быть русской раскладки


#7
print("Хемингуэй".index("м"))


#8
print("Не без горечи припомнились слова Хавата: \"Более всего ужасет враг, которым ты восхищаешься\".")
print('Не без горечи припомнились слова Хавата: "Более всего ужасет враг, которым ты восхищаешься".')

#9
tri="три"
print(tri+tri+tri)
print(tri*3)

#10
a="И незачем так орать! Я и в первый раз прекрасно слышал."
print(a.index("!")) #19
print(a[:19])