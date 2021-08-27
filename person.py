class Person:
    def __init__(self, first_name, last_name, birthdate, email):
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.email = email

    def eat(self):
        return "Today we are gonna eat cake because it's {} {}'s birthday .".format(self.birthdate, self.first_name)    
        
    def speak(self, sound):
        return "For {}'s birthday we sang to him {}.".format(self.first_name, sound)   

    def walk(self):
        return "{} walked from home to school.".format(self.first_name)

Tommy = Person ("Tommy","Snell","26th January","tonysnell@gmail.com")   
Craig = Person ("Craig","Broadshaw","25th May", "craigbr@hotmail.com")
Eli = Person ("Eli", "Vogli","16th January","elvedinvogli@gmail.com")

print(Tommy.eat())
print(Tommy.speak("Happy Birthday"))
print(Tommy.walk())
