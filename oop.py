# mylist = [1,2,3]
# mylist.append(4)
# print(mylist)
#
# print(type(mylist))
# print(type([]))
# print(type({}))
# print(type(()))
# print(type(0.2))
# print(type(2))
# CLASS
# class Sample():
#     pass
#
# x = Sample()
# print(type(x))

# class Dog():
#
#     # CLASS OBJECT ATTRIBUTE
#     species = "mammal"
#
#
#     def __init__(self,breed,name):
#         self.breed = breed
#         self.name = name
#         pass
#
#
#
# # mydog = Dog(breed='Lab',name='Sam')
# mydog = Dog('Lab','Sam')
# # otherdog = Dog(breed='Husky')
# print(mydog.breed)
# # print(otherdog.breed)
# print(mydog.name)
# print(mydog.species)

# class Circle():
#     pi = 3.14
#
#     def __init__(self,radius=1):
#         self.radius = radius
#
#     # METHOD
#     def area(self):
#         return self.radius*self.radius*Circle.pi
#
#     def set_radius(self,new_r):
#         self.radius = new_r
#
# mycircle = Circle(3)
# # mycircle.radius = 100
# # mycircle.set_radius(999)
# # print(mycircle.radius)
# print(mycircle.area())



# INHERITANCE
# class Animal():
#     def __init__(self):
#         print('ANIMAL CREATED')
#
#     def identify(self):
#         print('Animal')
#
#     def eat(self):
#         print('Eating')
#
# class Dog(Animal):
#
#     def __init__(self):
#         # Animal.__init__(self)
#         print("DOG CREATED")
#
#     # adding a new method
#     def bark(self):
#         print('WOOF')
#
#     # override method eat
#     def eat(self):
#         print("DOG EATING")

# mya = Animal()
# mya.identify()
# mya.eat()

# mydog = Dog()
# mydog.identify()
# mydog.eat()
# mydog.bark()


# PYTHON SPECIAL METHODS
# class Book():
#
#     def __init__(self,title,author,pages):
#         self.author = author
#         self.title = title
#         self.pages = pages
#
#     # special methods
#     def __str__(self):
#         return "Title: {}, Author: {}, Pages: {}".format(self.title,self.author,self.pages)
#
#     def __len__(self):
#         return self.pages
#
#     def __del__(self):
#         print('A book is destroyed')
#
# b = Book('python','jose',200)
# print(b)
# print(len(b))
# # delete an object like this
# del b