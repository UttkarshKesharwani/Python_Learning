
#!  Lists in python (same as array but store any value of any data types) :- A built in data type that stores set of values . It can store elements of different types (int,float,string , etc) . It is mutable 

student = ["karan",94.5,17,"Agra"]
print(student)
print(type(student))
print(student[0])

student[0]= "Uttkarsh"  #! allowed in python as list is immutable 

print(student)

#! List also supports "slicing" same as "string"
# list_name[ starting_idx : ending_idx ] #! ending idx is not included , it returns the value from starting to ending-1 idx

marks = [87,64,33,95,76]

print(marks[1:4])
print(marks[:4]) #! is same as marks[0:4]
print(marks[1:]) #! is same as marks[1:len(marks)]
print(marks[-3:-1]) #! [33,95]

#! some builtin "list Methods"

list = [2,1,3,1]

list.append(4) #! adds one element at the end 
print(list)

list.sort()  #! sorts in ascending order 

list.sort(reverse=True) #! sorts in descending order  

list.reverse() #! reverses list 

list.insert(2,4) #! insert element at index ( syntax :- list_name.insert(idx,ele) )
print(list)

list.remove(1) #! removes first occurences of element
print(list)

print(list.pop(2)) #! Remove and return item at index ( list_name.pop(idx) )
print(list)








#! Tuples :- A builtin data type that lets us create immutabel sequences of values while list is mutable 


tup1 = (1,2,3,4);
# tup = (1,) #! single value ke sath comma lagaya jata h nai to vo tuple nhi consider hoga agr tmne comma hata diya to 


print(tup1)
print(tup1[0])
print(tup1[1])
print(type(tup1));

# tup1[0] = 5 #! not allowed bcoz tuples are immutable 

#! Slicing in tuples is same as the slicing in list/string , it slice the tup and return the sliced value 
# tup_name[ starting_idx : ending_idx ] #! ending idx is not included , it returns the value from starting to ending-1 idx


tup=(7,5,6,2,7,8);

print(tup[1:3]);

#! builtin "Tuples Methods"

print(tup.index(7)) #! return index of first occurence of ele

print(tup.count(7)) #! counts total occurences of ele

