class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return "{} is {} years old".format(self.name,self.age)    

    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

mikey = Dog ("Mikey", 6)
jimmy = Dog ("Jimmy", 10)

print(mikey.description())
print(mikey.speak("Gruff Gruff"))
print(jimmy.description())
print(jimmy.speak("Wuff Wuff"))
