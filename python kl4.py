list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

def fun_list(l):
    even_list = []
    odd_list = []
    for x in l:
        if x % 2 == 0:
            even_list.append(x)
        else:
            odd_list.append(x)    
    return even_list, odd_list

print(fun_list(list))            

print("-------------------")

a = [1,1,2,3,5,8,13,21,34,55,89]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13]

def intersection(a,b):
    c = []
    for x in a:
        if x in b:
            c.append(x)
        else:
            c = set(c)    
    return c       
print(intersection(a,b))    
print("Lista pa duplikate is : " , intersection(a,b))

print("--------------")
a = [1,1,2,3,5,8,13,21,34,55,89]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13]

c = []
for x in a:
    for y in b:
        if x == y and x not in c:
            c.append(x)
print(c)            

print("----------------")

a = [1,1,2,3,5,8,13,21,34,55,89]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13]

set_a = set(a)
set_b = set(b)

print(set_a.intersection(set_b))
print ('-----------------')



lower_limit = input("Give us the lower limit: ")
upper_limit = input("Give us the upper limit: ")

for i in range(int(lower_limit),int(upper_limit)):
    print(i, end = " ")

print('----------')
