class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
student1= Student('Jason',12)
student2= Student("Jeffrey",18)

print(student1.name,student1.age)
print(student2.name,student2.age)

if (student1.age)>(student2.age):
    print("{} is older.".format(student1.name))
else:
    print("{} is older.".format(student2.name))



