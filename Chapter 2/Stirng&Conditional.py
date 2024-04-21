
str1 = "This is a stirng .\n Creating in python"
str2 = 'Uttkarsh kesharwani'
str3 = """This is also a string"""

print(str1);
print(len(str1))  #! gives 38 bcoz of indexing happens i.e every character has a index starting from 0 
print(str1[0])

# str1[0]="h" #! this is not allowed as string is immutabel in python




# ! Slicing :- Accessing parts of a string is known as slicing 
#   str[ starting_idx : ending_idx ] #! ending idx is not included

str = "Uttkarsh Kesharwani";
print(str[6:10]) #! return vlaue from index 6 to 9 (10 will not included)
print(str[6:len(str)]) #! or print(str[6:]) is same 
print(str[:10]) #! same as print(str[0:10]) python will put 0 automatically

# ! Note :- Python also support negative indexing while slicing starting from -1 from the last 
str4 = "Apple"
print(str4[-3:-1])
print(str4[-3:])
print(str4[:-3])

#! some builtin "Sting Functions"

str5 = "hey this is python"

print(str5.endswith("thon")) #! returns true if string ends with substr else false 

print(str5.capitalize()) #! capitalizes 1st char of string and return a new stirng with 1st char capatalize , it doesnt modify the original string
print(str5)

print(str5.replace("s","a")) #! repalces all occurences of old with new , it doesnt modify original string ,  syntax:- str5.replace(old,new)
print(str5.replace("python","javascipt"))
print(str5)

print(str5.find("is")) #! returns 1st index of 1st occurence

print(str5.count("is")) #! counts the occurence of substrings you provided and returns count



# ! Conditional Statement 
 
# if-elif:-  

#if condition1:
    # Code block to execute if condition1 is True
#elif condition2:
    # Code block to execute if condition1 is False and condition2 is True
#else:
    # Code block to execute if both condition1 and condition2 are False

x=110;

if(x>10):
  print("x is greater than 10")
  print("hehe")
elif x==10:
  print("x is equal to 10")
else:
  print("x is less than 10")




marks = int(input("Enter your marks"));

if(marks >= 90):
  grade ="A"
elif(marks>=80 and marks<90):
  grade ="B"
elif(marks>=70 and marks<80):
  grade ="C"
else:  
  grade="D"

print("Grade of student is ",grade)


