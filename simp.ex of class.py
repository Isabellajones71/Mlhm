class Dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def bark(self):
        return "rrr rrrr"

ozzy = Dog('ozzy',2)
print(ozzy.name)
print("{} barks {}" . format(ozzy.name,ozzy.bark()))
print(ozzy.age)


