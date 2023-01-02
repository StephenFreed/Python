
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

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Person:
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


jack = Person('Jack', 'Harlow', 26)
yeah = hasattr(jack,"first_name")
yeah2 = getattr(jack, "nope", 500)

print(type(jack))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Student:

  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []
    
  def add_grade(self, grade):
    if type(grade) is Grade:
      self.grades.append(grade)

class Grade:

  minimum_passing = 65
  def __init__(self, score):
    self.score = score

  def list_grades(self):
    listy = [str(grade.core) for grade in self.grades]
    return listy
  
roger = Student('Roger van der Weyden', 10)
sandro = Student('Sandro Botticelli', 12)
pieter = Student('Pieter Bruegel the Elder', 8)

pieter.add_grade(Grade(100))
print(roger)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class SearchEngineEntry:
  def __init__(self, url):
    self.url = url
 
codecademy = SearchEngineEntry("www.codecademy.com")
wikipedia = SearchEngineEntry("www.wikipedia.org")
 
print(codecademy.url)
# prints "www.codecademy.com"
print(wikipedia.url)
# prints "www.wikipedia.org"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

 
"""
Attributes can be added to user-defined objects after instantiation, so it’s possible 
for an object to have some attributes that are not explicitly defined in an object’s constructor. 
We can use the dir() function to investigate an object’s attributes at runtime. 
dir() is short for directory and offers an organized presentation of object attributes.
That’s certainly a lot more attributes than we defined! Python automatically adds a number 
of attributes to all objects that get created. These internal attributes are usually 
indicated by double-underscores. But sure enough, attribute is in that list.

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
e1.name


# python does not have method overloading only overriding
# you would need if statements on type() or *arg length to sudo method override
# pythong has multi-level inheritance Organism -> Animal(Organism) -> Dog(Animal)
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

class Person:
    def noise(self):
        print('Person does this.')

an_animal = Animal('Animal')
my_lion = Lion('Badass Lion')
my_cat = Cat("Kitty")
my_person = Person()
yeah = [an_animal,my_lion,my_cat,my_person]

for elm in yeah:
    elm.noise()

my_person.noise()

print(Animal.age)
a = Animal("Tiger")
print(a.name)
print(a.noise())
print(a.age)





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

print(repr(phillipsburg))




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
print(stephen.name)
print(stephen.age)
print(stephen._social_security)  # still able to access protected attribute
stephen.set_social_security(9999999)  # setting new social
print(stephen.get_social_security())  # getting social


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
print(stephen.name)
print(stephen.age)
# print(stephen.__social_security)  # trying to access private attribute throws error
stephen.set_social_security(9999999)  # setting new social
print(stephen.get_social_security())  # getting social
