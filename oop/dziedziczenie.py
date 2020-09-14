class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Dog(Animal):
    def voice(self):
        print("Hau hau")

class Wolf(Dog):
    def getVoice(self):
        print("Jestem wilkiem")
        super().voice() #super() - tak jak self ale w klasie z której dziedziczy ta klasa

class Cat(Animal):
    def getVoice(self):
        print("Miau miau") 


dog = Dog("Reksio", 10)
print(dog.name)
print(dog.age)
dog.voice()
wolf = Wolf("Henryk", 10)
wolf.getVoice()
