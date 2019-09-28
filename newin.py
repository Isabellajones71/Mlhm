class Dog:

    # methods of the parent class
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def des(self):
        return "{} is {} years old" .format(self.name,self.age)

#Child class
class Bulldog(Dog):
    #method of a child class
    def __init__(self):
        super().__init__()
        print("Beware I am a bull dog")

    def run(self,speed):
        return "{} runs in {}speed" .format(self.name,speed)
