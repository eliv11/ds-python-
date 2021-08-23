counter = 1 

while counter < 11:
   print(counter) 
   counter += 1


   #for loops
   students = ['Almira','Agon','Drilon']
   grades = ['1','2','3','4','5']
   name = 'Agon'
   for x in name:
       print(x)
   for student in students:
       print(student)

for x in grades:
        print(x)   
for x in range(6):
    print(x)        
for x in range(5, 12):
    print(x)    

#detyre 
# #using while loops print only even numbers between 1 and 100
print('_________________________')    
num = 1
even_counter = 0
odd_counter = 0
while num <= 100:
    if num % 2 == 0:
        even_counter += num
    else:
        odd_counter += num  
    num += 1
print("Total sum of even numbers is:", even_counter )  
print("Total sum of odd numbers is:", odd_counter)  


