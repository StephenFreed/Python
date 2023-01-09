
"""
A class doesn’t accomplish anything simply by being defined. A class must be instantiated.
A class is a template for a data type. It describes the kinds of information that 
class will hold and how a programmer will interact with that data

When we want the same data to be available to every instance of a class we use a class variable. 
A class variable is a variable that’s the same for every instance of the class.

Methods are functions that are defined as part of a class. The first argument in a 
method is always the object that is calling the method. Convention recommends that 
we name this first argument self. Methods always have at least this one argument.

The data held by an object is referred to as an instance variable. Instance variables 
aren’t shared by all instances of a class — they are variables that are specific to the object they are attached to.
"""



class PersonClass:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age 
    
    def __repr__(self):
        return "{} {}".format(self.first_name, self.last_name)
    
    def talk(self):
        print('{} is talking'.format(self.first_name))

    def get_last_name(self):
        print("{}\'s last name is {}".format(self.first_name, self.last_name))

foo = PersonClass("Foo", "Bar", 20)
first_name_attribute = hasattr(foo, "first_name")
get_class_attribute = getattr(foo, "first_name", 500)

# print(type(foo))
# print(foo)
# print(first_name_attribute)
# print(get_class_attribute)
# print(foo.talk())
# print(foo.get_last_name())



class Student:

  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
    
  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)

  def get_grades(self):
      grade_list = []
      for grade in self.grades:
          grade_list.append(grade)
      print(grade_list)

class Grade:
  minimum_passing = 65
  def __init__(self, score):
    self.score = score

  
student_foo = Student("Foo", 10)
stduent_bar = Student("Bar", 12)
student_baz = Student("Baz", 8)

student_foo.add_grade(Grade(100))
student_foo.add_grade(Grade(80))
student_foo.add_grade(Grade(90))
student_foo.get_grades()



class SearchEngineEntry:
  def __init__(self, url):
    self.url = url
 
bar_website = SearchEngineEntry("www.foo.com")
foo_website = SearchEngineEntry("www.bar.org")
# print(foo_website.url)
# print(bar_website.url)


# dunder methods are built in python object methods
# we can override these methods in our classes to get the functionality we want

class NoDunderOverrides:
    x = 5
    y = 10


print("~~~~~ No Dunder Override ~~~~~")
no_dunder = NoDunderOverrides
print(no_dunder)


class DunderOverride:
    x = 5
    y = 10

    # this overrides __init__ passing in self object and arguments to hold
    def __init__(self, name="no name yet", age="no age yet"):
        self.name = name
        self.age = age

    def __repr__(self):
        return "I Am DunderOverride Class"

    def __len__(self):
        return 99


print("~~~~~ Dunder Override ~~~~~")
duner_override = DunderOverride("Stephen")
print(duner_override)
print(len(duner_override))
print(duner_override.name)
print(duner_override.age)


 
"""
Attributes can be added to user-defined objects after instantiation, so it’s possible 
for an object to have some attributes that are not explicitly defined in an object’s constructor. 
We can use the dir() function to investigate an object’s attributes at runtime. 
dir() is short for directory and offers an organized presentation of object attributes.
Python automatically adds a number of attributes to all objects that get created. These internal attributes are usually 
indicated by double-underscores. 

Do you remember being able to use type() on Python’s native data types? This is because they are 
also objects in Python. Their classes are int, float, str, list, and dict. These Python classes 
have special syntax for their instantiation, 1, 1.0, "hello", [], and {} specifically. 
But these instances are still full-blown objects to Python.

We implemented the __repr__() method and had it return the .name attribute of the object. 
When we printed the object out it simply printed the .name of the object! Cool!
"""

# getters and setters
class Employee():

    def __init__(self,name = 'Name:'):
        self.__name = name
    
    @property
    def name(self):
        print(self.__name)

    @name.setter
    def name(self,new_name):
        self.__name = new_name 

    @name.deleter
    def name(self):
        del self.__name
    


e1 = Employee()

e1.name = 'Billy'

del e1.name
e1.name = 'Bob'
# e1.name


# python does not have method overloading only overriding
# you would need if statements on type() or *arg length to sudo method override
# python has multi-level inheritance Organism -> Animal(Organism) -> Dog(Animal)
# multiple inheritance Dog(Animal,Organism)
# method chaining / method must return self

class Animal:
    age = 10  # class variable

    def __init__(self,name):
        self.name = name  # instance variable
    def noise(self):
        print('{} does animal noises'.format(self.name))

class Lion(Animal):
    def noise(self):
        print('{} goes roooaarrrr'.format(self.name))

class Cat(Animal):
    def noise(self):
        print('{} going prrrrrr'.format(self.name))

class SomePerson:
    def noise(self):
        print('Person does this.')

an_animal = Animal('Animal')
my_lion = Lion('Lion')
my_cat = Cat("Kitty")
my_person = SomePerson()
class_list = [an_animal,my_lion,my_cat,my_person]

# for elm in class_list:
#     elm.noise()

# print(Animal.age)
# a = Animal("Tiger")
# print(a.name)
# print(a.noise())
# print(a.age)





class School:
    def __init__(self, name, level, number_of_students):
      self.name = name
      self.level = level
      self.number_of_students = number_of_students

    def get_name(self):
      print(self.name)

    def get_level(self):
      print(self.level)

    def get_number_of_students(self):
      print(self.number_of_students)
    
    def set_number_of_students(self, number_students):
      self.number_of_students = number_students

    def __repr__(self):
      return 'A {} school name {} with {} students.'.format(self.level,self.name,self.number_of_students)
      
    def __str__(self):
      return 'yeahh'


class PrimarySchool(School):
    def __init__(self, name, number_of_students, pickup_policy):
      super().__init__(name, 'Primary', number_of_students)
      self.pickup_policy = pickup_policy

    def get_pickup_policy(self):
      print(self.pickup_policy)

    def __repr__(self):
      return 'A Primary school {} with {} students and {} pickup policy.'.format(self.name,self.number_of_students,self.pickup_policy,self.pickup_policy)



class HighSchool(School):
    def __init__(self, name, number_of_students, pickup_policy, sports_teams):
      super().__init__(name, 'High School', number_of_students)
      self.pickup_policy = pickup_policy
      self.sports_teams = sports_teams

    def get_sports_teams(self):
      print(self.sports_teams)

    def __repr__(self):
      return 'A {} school {} with {} students and {} pickup policy and {} sports.'.format(self.level,self.name,self.number_of_students,self.pickup_policy,self.pickup_policy,self.sports_teams)



phillipsburg = HighSchool('Phillipsbug','High School', '500',['football','soccer','baseball'])
lopat = PrimarySchool('Lopat', '100', 'Yes')

# print(repr(phillipsburg))




# ~~~~~~~~~~ Protected Access Modifier ~~~~~~~~~~

# one _ before variable or method signifies protected access

class Person:

    name = None
    age = None
    # protected instance variable
    _social_security = None

    # constructor
    def __init__(self, name, age, social_security):
        self.name = name
        self.age = age
        self._social_security = social_security

    # protected should have getters and setters
    def set_social_security(self, social_security):
        self._social_security = social_security

    def get_social_security(self):
        return self._social_security


stephen = Person("Stephen", 36, 12345)
# print(stephen.name)
# print(stephen.age)
# print(stephen._social_security)  # still able to access protected attribute
stephen.set_social_security(9999999)  # setting new social
# print(stephen.get_social_security())  # getting social


# ~~~~~~~~~~ Private Access Modifier ~~~~~~~~~~

# two __ before variable or method signifies private access


class PrivatePerson:

    name = None
    age = None
    # private instance variable
    __social_security = None

    # constructor
    def __init__(self, name, age, social_security):
        self.name = name
        self.age = age
        self.__social_security = social_security

    # private must have getters and setters
    def set_social_security(self, social_security):
        self.__social_security = social_security

    def get_social_security(self):
        return self.__social_security


stephen = PrivatePerson("Stephen", 36, 12345)
# print(stephen.name)
# print(stephen.age)
# print(stephen.__social_security)  # trying to access private attribute throws error
stephen.set_social_security(9999999)  # setting new social
# print(stephen.get_social_security())  # getting social
