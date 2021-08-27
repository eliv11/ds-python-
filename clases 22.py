class Dog:
    def __init__(self, name , age):
        self.name = name
        self.age = age 


    
jake = Dog ("Jake", 7)
dag = Dog ("Dag", 5)
william = Dog ("William", 6)



def get_biggest_number(*args):
    return max(args)

print("The oldest dog is {} years old.".format(get_biggest_number(jake.age, dag.age, william.age)))    