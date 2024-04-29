

# ! Loops in python

#! syntax of while loop :-
#   while condition :
#     Statement to be executed


# ! printing 1 to 10 using while loop
i = 1
while i<=10:
  print("hello world from python")
  i +=1 
  print(i)

print("\n")

# ! printing from 1 to 100
count=1
while True:
  if(count > 100):
    break;
  else:
    print(count)
    count+=1



# ! printting the multiplication table of a number "n"
num = int(input("enter which table you want to print"))
n=1
while(n<=10):
  print(f"{num}*{n} = {num*n}")
  n+=1;

# ! print the element of the following list using a loop :- [1,4,9,16,25,36,49,64,81,100]

list = [1,4,9,16,25,36,49,64,81,100]
q= len(list)-1
ind = 0 
while(ind<=q):
  print(f"value at {ind}th index is :- {list[ind]}");
  ind +=1


# ! search for a number "x" in this tuple using loop :- [1,4,9,16,25,36,49,64,81,100]
tuple = (1,4,9,16,25,36,49,64,81,100)

val = int(input("Enter the value u want to find in the tuple:-"));
# val=49;
ind=0
while(ind<len(tuple)):
  if(tuple[ind]==val):
    print(f"value is present at {ind}th index");
    break;
  ind=ind+1;

if(ind==len(tuple)):
  print("value is not present in the tuple");



# ! Range in python :- 

# ! range() :- range function return a sequence of numbers  , starting from 0 by default , and increments by 1 (by default) , and stops before a specified number
# ! syntax :- range(start?,stop, step?) , jha pr questino marks lga hai , vo parameter optional hota hai 

seq = range(5) #! will store like  seq[0],seq[1],seq[2]... and so on 
for i in seq:
  print("val stored in seq is:- ",i)


for i in range(2,11,2): #! Printing all even no b/w 1 to 10 
  print(i); 

for i in range(101): #! printing from 0 to 100
  print(i)  

print("printing from 100 to 0");
for i in range(100,-1,-1): #! printing from 100 to 0
  print(i) 

val = int(input("enter the val to print the table of number using range:-"))
for i in range(1,11): #! printing the table of number using range 
  print(f"{val}*{i} = {val*i}")

n = 5
sum = 0
for i in range(n+1): #! sum the n natural no 
  sum += i ;

print("the sum of n natual no is :- ", sum )

#! printing factorial of no 
val = int(input("kiska factorial nikalna hai :-"))
fact = 1
for i in range(1,val+1):
  fact *= i 

print(f"factorial {val} ka hai :-",fact)

# ! For loop in python :-
 
list = [1,2,3];
for ele in list: #! here "ele" will have every value of a list of every index 
  print(f"Using for loop , value in list is :-",ele)
# ! same as 
for i in range(0,len(list)): #! printing from 1 to 101 using for loop  // Note :- in ragne(initial_idx , final_idx + 1); likhna hota hai  
  print("val of list using for loop ",list[i])


tuple =(1,2,3,4,5,6)
for i in range(1, 102): #! printing from 1 to 101 using for loop  // Note :- in ragne(initial_idx , final_idx + 1); likhna hota hai  
  print(i)

# 
str = "Uttkarsh kesharwani";
for char in str:
  print(char)
else:
  print("this will run when string str completely print")


#! Pass Statement :- Pass is a null statement that doesm nothing . It is used as a placeholder for future code .

for i in range(5):
  pass

if  i >>5:
  pass

print("after pass statement")