#Процедурное программирование
x=2
y=4
z=8
xyz=x+y+z
print(xyz)


rock=[]
country=[]

def collect_songs():
    song="Укажите песню."
    ask="Введите р (рок) или к (кантри). Введите Х для выхода."
    while True:
        genre=input(ask)
        if genre=="Х":
            break
        if genre=="р":
            rk=input(song)
            rock.append(rk)
        elif genre=="к":
            cy=input(song)
            country.append(cy)
        else:
            print("Неверно.")
    print(rock)
    print(country)
collect_songs()
            

a=0
def increment():
    global a
    a+=1

#Функциональное программирование
def increment2(b):
    return b+1
increment2(6)

#ООП
class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        self.mold=0
        print("Created!")
    def rot(self, days, temp):
        self.mold= days*temp
        
or1=Orange(10, "dark orange") #Created!
print(or1) #<__main__.Orange object at 0x00000210B32E2370>
or1.weight=100
or1.color="light orange"
print(or1.weight)
print(or1.color)

or2=Orange(4, "light orange")
or3=Orange(8, "dark orange")
or4=Orange(14, "yellow orange")

or5=Orange(6, "orange")
print(or5.mold)
or5.rot(10, 33)
print(or5.mold)
print(type(or1))



class Rectangle:
    def __init__(self, w, l):
        self.width=w
        self.len=l
    def area(self):
        return self.width*self.len
    def change_size(self, w, l):
        self.width=w
        self.len=l
        
rectangle=Rectangle(10,20)
print(rectangle.area())
rectangle.change_size(20,40)
print(rectangle.area())


#1
class Apple:
    def __init__(self, w, c, d, s):
        self.weight=w
        self.color=c
        self.diameter=d
        self.sort=s
        print("Created!")
ap1=Apple(30, "red", 7, "Polish")
ap2=Apple(50, "green", 5, "Jonagold")


#2
import math
class Circle:
    def __init__(self,r):
        self.radius=r
    def area(self):
        return math.pi*self.radius**2

cr1=Circle(2)
print(cr1.area())


#3
class Triangle:
    def __init__(self, b, h):
        self.base=b
        self.height=h
    def area(self):
        return 0.5*self.base*self.height

tr1=Triangle(5, 3)
print(tr1.area())


#4
class Hexagon:
    def __init__(self,a,b,c,d,e,f):
        self.sidea=a
        self.sideb=b
        self.sidec=c
        self.sided=d
        self.sidee=e
        self.sidef=f
    def calculate_perimeter(self):
        return self.sidea+self.sideb+self.sidec+self.sided+self.sidee+self.sidef

hx1=Hexagon(1,2,3,4,5,6)
print(hx1.calculate_perimeter())
        