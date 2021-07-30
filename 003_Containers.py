print('Hello'.upper())
print('Hello'.replace('e','@'))

#Список
print(list('Hello'))

fruit=list()
print(fruit)

fruit=[]
print(fruit)

fruit=['Apple','Orange','Peach']
print(fruit)
fruit.append('Banana')
fruit.append('Melon')
print(fruit)
print(fruit[0])
print(fruit[1])
print(fruit[2])

#Use the insert method to add "lemon" as the second item in the fruits list.
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")
print(fruits)


#Use a range of indexes to print the third, fourth, and fifth item in the list.
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

random=[]
random.append(True)
random.append(100)
random.append(1.1)
random.append('Hello')
print(random)

colors=['blue','green','yellow']
#print(colors[4]) #IndexError: list index out of range
print(colors)
colors[2]='red'
print(colors)

colors=['blue','green','yellow']
print(colors)
item=colors.pop()
print(item) #yellow
print(colors) #['blue', 'green']

colors1=['blue','green','yellow']
colors2=['orange','pink','black']
print(colors1+colors2)
print('green' in colors1)
print('black' not in colors1)
print(len(colors1)) #3

colors=['violet','orange','green']
guess=input('Guess the color: ')
if guess in colors:
    print('You\'ve guessed it!')
else:
    print('Wrong! Try again.')
    
#Кортежи
my_tuple=tuple()
print(my_tuple)

my_tuple=()
print(my_tuple)

rndm=('M. Jackson',1958,True)
print(rndm)

#this is a tuple
a=('self_taught',) #('self_taught',)
print(a)
#this is not a tuple
(9)+1 #10

dys=('1984','Brave New World','Fahrenheit 451')
#dys[1]='Handmaid\'s tale' #TypeError: 'tuple' object does not support item assignment
print(dys[2])
print('1984' in dys)
print('Handmaid\'s tale' not in dys)

#Словари
my_dict=dict()
print(my_dict)

my_dict={}
print(my_dict)

fruits={'Apple':
        'red',
        'Banana':
        'yellow'}
print(fruits)

facts=dict()
#add a value
facts['code']='funny'
#look up a key
print(facts['code'])
facts['Bill']='Gates'
print(facts['Bill'])
facts['foundation']=1776
print(facts['foundation'])

bill=dict({'Bill Gates':
           'generous'})
print('Bill Gates' in bill)
print('Bill Doors' not in bill)

books={'Dracula':'Stoker',
       '1984':'Orwell',
       'Process':'Kafka'}
del books['Process']
print(books)


rhymes={'1':'fun',
        '2':'blue',
        '3':'me',
        '4':'floor',
        '5':'life'
}

n=input('Enter a number: ')
if n in rhymes:
    rhyme=rhymes[n]
    print(rhyme)
else:
    print('Not found.')
    
    
#Контейнеры внутри контейнеров
lists=[]
rap=['Eminem',
     'Kendrick Lamar',
     'Snoop Dogg',
     '50 Cent']

rock=['The Beatles',
      'Led Zeppelin',
      'Pink Floyd']

djs=['Fatboy Slim',
     'Sasha & John Digweed']
lists.append(rap)
lists.append(rock)
lists.append(djs)
print(lists)

rap=lists[0]
print(rap)

rap.append('Ice Cube')
print(rap)
print(lists)


locations=[]
tula=(54.1960,37.6182)
moscow=(55.7522,37.6155)
locations.append(tula)
locations.append(moscow)
print(locations) #[(54.196, 37.6182), (55.7522, 37.6155)]


eights=['Edgar Allan Poe',
        'Charles Dickens']
nines=['Hemingway',
       'Fitzgerald',
       'Orwell']
authors=(eights,nines)
print(authors) #(['Edgar Allan Poe', 'Charles Dickens'], ['Hemingway', 'Fitzgerald', 'Orwell'])


bday={'Hemingway':
      '21.07.1899',
      'Fitzgerald':
      '24.09.1896'}
my_list=[bday]
print(my_list)
my_tuple=(bday,)
print(my_tuple)


ru={'location':
    (55.7522,
     37.6155),
    
    'famous people':
    ['Andrei Zvjagintsev',
     'Yuri Bykov',
     'Pyotr Buslov'],
    
    'facts':
    {'city':
     'Moscow',
     'country':
     'Russia'}
}
    
print(ru['location'])
print(ru['famous people'])
print(ru['facts'])


#1
musicians=[]
musicians.append('Laibach')
musicians.append('Tears For Fears')
musicians.append('Einstürzende Neubauten')
print(musicians)

musicians=['Laibach', 'Tears For Fears', 'EN']
print(musicians)

#2
Sillamae=(59.3931, 27.7742)
Tartu=(58.3780, 26.7285)
Tallinn=(59.4370, 24.7536)
Moscow=(55.7512, 37.6184)
places=[Sillamae, Tartu, Tallinn, Moscow]
print(places)

locations = [(40.7128, 74.0059), (31.0461, 34.8516), (8.3405, 115.0920)]

#3
angelina={
    'height':'1.58m',
    'favourite color':'pink',
    'favourite actor':'Leonardo DiCaprio'
}
print(angelina)
print(angelina['height'])


#4
angelina['height']=input('Insert your height: ')
angelina['favourite color']=input('Insert your favourite color: ')
angelina['favourite actor']=input('Insert your favourite actor: ')
print(angelina)

key = input('What do you want to know about Angelina? Is it height, favourite color or favourite actor? \n')
if key in angelina:
    result = angelina[key]
    print(result)

#5
music_dictionary={
    'Laibach':['Eurovision', 'Koran', 'Americana'],
    'Tears For Fears':['Woman in Chains', 'Famous Last Words', 'Swords And Knives'],
    'EN':['Sabrina','Die Interimsliebenden','Die Befindlichkeit des Landes']
}
print(music_dictionary)
for x in music_dictionary:
  print(x)

#6 Множества
thisset = {"apple", "banana", "cherry"}
print(thisset)


thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
print(len(thisset))

thisset = {"apple", "banana", "cherry"}
print(len(thisset))


set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}


set1 = {"abc", 34, True, 40, "male"}
type(set1) #set

thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)


#You cannot access items in a set by referring to an index or a key.
#But you can loop through the set items using a for loop,
#or ask if a specified value is present in a set, by using the in keyword.

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

print("banana" in thisset)

thisset.add("orange")
print(thisset)


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)


thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)


#Note: If the item to remove does not exist, remove() will raise an error.
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)


#Note: If the item to remove does not exist, discard() will NOT raise an error.
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)


#You can also use the pop() method to remove an item,
#but this method will remove the last item. Remember that sets are unordered,
#so you will not know what item that gets removed.
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)


thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)


thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)

#Note: Both union() and update() will exclude any duplicate items.
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)


#The intersection_update() method will keep only the items 
#that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

#The intersection() method will return a new set, that only contains
#the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

#The symmetric_difference_update() method will keep only the elements that
#are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)

#The symmetric_difference() method will return a new set, that contains only
#the elements that are NOT present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)


#Return True if no items in set x is present in set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)

