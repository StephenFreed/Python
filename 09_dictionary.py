"""
dictionaries are used to store data values in key:value pairs.

a dictionary is a collection which is ordered*, changeable and do not allow duplicates

as of python version 3.7, dictionaries are ordered. in python 3.6 and earlier, dictionaries 
are unordered.
"""


my_dictionary = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(my_dictionary)


menu = {"Foo": 1, "Bar": 2, "Baz": 2}


students_in_classes = {
        "software design": ["Aaron", "Delila", "Samson"],
        "history": ["Christopher", "Juan", "Marco"],
        "philosophy": ["Frederica", "Manuel"]
        }
print(students_in_classes)


sensors = {}
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
print(sensors)


print(sensors.get("pantry"))

sensors.pop("pantry")
print(sensors)

print(sensors.keys())

print(sensors.values())

print(sensors.items())

sensors.clear()
print(sensors)
