#Encapsulation
class Rectangle():
    def __init__(self, w, l):
        self.width=w
        self.len=l
    def area(self):
        return self.width*self.len



class Data:
    def __init__(self):
        self.nums=[1,2,3,4,5] #список
    def change_data(self,index,n):
        self.nums[index] = n
        
data_one = Data()
data_one.nums[0] =100
print(data_one.nums)

data_two = Data()
data_two.change_data(0, 100)
print(data_two.nums)



class Data:
    def __init__(self):
        self.nums=(1,2,3,4,5) #кортеж/tuple
    def change_data(self,index,n):
        self.nums[index] = n      
data_one = Data()
data_one.nums[0] =100
print(data_one.nums)



class PublicPrivateExample:
    def __init__(self):
        self.public="safe"
        self._unsafe="unsafe"
    def public_method(self):
        #clients can use this
        pass
    def _unsafe_method(self):
        #clients must not use this
        pass
        self.public="safe"
        self._unsafe="unsafe"
        
PublicPrivateExample_one=PublicPrivateExample()
PublicPrivateExample_one.public="safe1"
PublicPrivateExample_one.public_method()
print(PublicPrivateExample_one.public)

PublicPrivateExample_one._unsafe="unsafe1" #менять на свой страх и риск
#PublicPrivateExample_one._unsafe_method()
print(PublicPrivateExample_one._unsafe)




#Abstraction



#Polymorphism
print("Hello,world!")
print(200)
print(200.1)

print(type("Hello,world!"))
print(type(200))
print(type(200.1))

#Рисование фигур без полиморфизма
shapes=[tr1,sq1,cr1]
for a_shape in shapes:
    if type(a_shape)=="Triangle":
        a_shape.draw_triangle()
    if type(a_shape)=="Square":
        a_shape.draw_square()
    if type(a_shape)=="Circle":
        a_shape.draw_circle()
        
#Рисуем фигуры с помощью полиморфизма
shapes=[tr1,sq1,cr1]
for a_shape in shapes:
    a_shape.draw()


#Inheritance
class Shape():
    def __init__(self,w,l):
        self.width=w
        self.len=l
    def print_size(self):
        print("""{} на {}
              """.format(self.width,self.len))

my_shape=Shape(20,25)
my_shape.print_size()

class Square(Shape):
    pass

a_square=Square(20,20)
a_square.print_size()

class Square(Shape):
    def area(self):
        return self.width*self.len
a_square=Square(20,20)
print(a_square.area())

#Переопределение метода

class Square(Shape):
    def area(self):
        return self.width*self.len
    def print_size(self):
        print("""Я {} на {}
              """.format(self.width,self.len))
a_square=Square(20,20)
a_square.print_size() #не print(a_square.print_size())



#Composition
class Dog():
    def __init__(self,name,breed,owner):
        self.name=name
        self.breed=breed
        self.owner=owner
        
class Person():
    def __init__(self, name):
        self.name=name
        
mick=Person("Mick Jagger")
stan=Dog("Stanley","Bulldog",mick)
print(stan.owner.name)

#1
class Rectangle():
    def __init__(self,side_a,side_b):
        self.side_a=side_a
        self.side_b=side_b
    def calculate_perimeter(self):
        return (self.side_a+self.side_b)*2
        
class Square():
    def __init__(self, side):
        self.side=side
    def calculate_perimeter(self):
        return self.side*4

rectangle1=Rectangle(2,5)
print(rectangle1.calculate_perimeter())

square1=Square(7)
print(square1.calculate_perimeter())
        


class Rectangle():
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def calculate_perimeter(self):
        return self.width * 2 + self.length * 2

class Square():
    def __init__(self, s1):
        self.s1 = s1
    def calculate_perimeter(self):
        return self.s1 * 4

a_rectangle = Rectangle(25, 50)
a_square = Square(20)

print(a_rectangle.calculate_perimeter())
print(a_square.calculate_perimeter())


#2
class Square():
    def __init__(self, side):
        self.side=side
    def calculate_perimeter(self):
        return self.side*4
    def change_size(self,number):
        self.side+=number
        #print(self.side)
        
square1=Square(7)
print(square1.side)
square1.change_size(-2)
print(square1.side)


#3
class Shape():
    def what_am_i(self):
        print("I'm a shape")
              
class Rectangle(Shape):
    def __init__(self,side_a,side_b):
        self.side_a=side_a
        self.side_b=side_b
    def calculate_perimeter(self):
        return (self.side_a+self.side_b)*2
        
class Square(Shape):
    def __init__(self, side):
        self.side=side
    def calculate_perimeter(self):
        return self.side*4
    
rectangle2=Rectangle(2,3)
square2=Square(5)
rectangle2.what_am_i()
square2.what_am_i()


#4
class Horse():
    def __init__(self,name,rider):
        self.name=name
        self.rider=rider
        
class Rider():
    def __init__(self,name):
        self.name=name

rider1=Rider("John Star")
horse1=Horse("Apple",rider1)
print(horse1.rider.name)



class Horse():
    def __init__(self, name):
        self.name = name
class Rider():
    def __init__(self, name, horse):
        self.name = name
        self.horse = horse

harry_the_horse = Horse("Гарри")
the_rider = Rider("Салли", harry_the_horse)
print(the_rider.horse.name)
