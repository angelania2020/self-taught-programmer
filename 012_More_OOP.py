# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 19:23:01 2021

@author: Angelina
"""

class Square:
    pass
print(Square)



class Rectangle():
    def __init__(self,w,l):
        self.width=w
        self.len=l
    def print_size(self):
        print("""{} на {}
              """.format(self.width,self.len))

my_rectangle = Rectangle(10,24)
my_rectangle.print_size()



class Rectangle():
    recs=[] #Переменная класса
    def __init__(self,w,l):
        self.width=w #Переменная экземпляра класса
        self.len=l
        self.recs.append((self.width,self.len))
    def print_size(self):
        print("""{} на {}
              """.format(self.width,self.len))

r1=Rectangle(10,24)
r2=Rectangle(20,40)
r3=Rectangle(100,200)
print(Rectangle.recs)
print(r3.recs)

#The append method can only append one item at a time, 
#by using using an additional set of parentheses you append one tuple 
#(tuple is an immutable list)

#if you want to add multiple elements at once, use list extending:
lst = [1, 2, 3,]
lst += [4, 5, 6]
print(lst)


class Lion:
    def __init__(self,name):
        self.name=name
        
lion=Lion("Dilbert")
print(lion)



class Lion:
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return self.name
        
lion=Lion("Dilbert")
print(lion)



class AlwaysPositive:
    def __init__(self, number):
        self.n=number
    def __add__(self, other):
        return abs(self.n+other.n)

x=AlwaysPositive(-30)
y=AlwaysPositive(10)
print(x+y)
print(x+5) #AttributeError: 'int' object has no attribute 'n'
print(5+y) #TypeError: unsupported operand type(s) for +: 'int' and 'AlwaysPositive'




class Person:
    def __init__(self):
        self.name="Bob"
        
bob=Person()
same_bob=bob
print(bob is same_bob)

another_bob=Person()
print(bob is another_bob)



x=10
if x is None:
    print("x equals None :(")
else:
    print("x does not equal None")
    
x=None
if x is None:
    print("x equals None :(")
else:
    print("x does not equal None")
    
    
#1
class Square:
    square_list=[]
    def __init__(self,s):
        self.side=s
        self.square_list.append(self.side)

sq1=Square(5)
sq2=Square(1)
sq3=Square(15)
print(Square.square_list)

#1
class Shape():
    def what_am_i(self):
        print("Я - фигура.")


class Square(Shape):
    square_list = []

    def __init__(self, s1):
        self.s1 = s1
        self.square_list.append(self)

    def calculate_perimeter(self):
        return self.s1 * 4

    #def what_am_i(self):
        #super().what_am_i()
        #print("Я - фигура.")


a_square = Square(29)
print(Square.square_list)
another_square = Square(93)
print(Square.square_list)
a_square.what_am_i()

#2
class Square:
    list=[]
    def __init__(self,s):
        self.side=s
        self.list.append(self.side)
    def __repr__(self):
        #return здесь!!!
        return """{} на {} на {} на {} 
              """.format(self.side,self.side,self.side,self.side)

sq4=Square(7)
print(sq4)


#3
def f(x,y):
    print (x is y)
f(2,2)
f(2,3)
f("hi",0.5)

#3
def compare(obj1, obj2):
    return obj1 is obj2
print(compare("а", "б"))


