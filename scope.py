name = "Elvedin Vogli"

def hello():
    name2 = "Drilon"
    print("Hello " + name)
    print("Hello " + name2)


hello()
print(name)
print("--------------------")
def min_max_number_in_list(list):
    max = list [0]
    min = list [0]
    for a in list:
        if a > max:
            max = a
        if a < min:
            min = a    
    return max,min
print(min_max_number_in_list([1, 2, -8, 5]))
print('-----------')

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

s = "Agon"

print("The original string is :" , end="")
print(s)

print("The reversed string(using loops) is : ",end="")
print(reverse(s))

print("----------------")

list = [10,15,25,50,60,75,3,9,14]

def even_sum(l):
    even_sum = 0
    for x in l:
        if x % 2 == 0:
         even_sum += 1
         
         
    return even_sum 

print("There are", even_sum(list), "even numbers.")


def odd():
    d = dict ();
    d['list'] = [1,3,5,7]
    d['sum'] = 16
    d['len_of_list'] = 4
    return d
print(odd())   

def even():
    d = dict ();
    d['list'] = [2,4,6]
    d['sum'] = 12 
    d['len_of_list'] = 3
    return d
print(even())    