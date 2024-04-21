
# ! Variable and Data Types


print("Hey i m uttkarsh " , "i m from khaga")
print("hello world")

print(23)  
print(type(23))  
print(55+30);



name = "Uttkarsh";
age = 21 

print("my name is : ",name);
print("my age is : ",age);



# ! Data Types :- 
#! => Integers , String , Float , Boolean , None 

age  = 23;
a = None
b = False 
print(type(age))
print(type(a))


# ! Taking input in python 
name = input("Enter your name");
print("your name is :- ", name);


age = input("Enter your age ");
print("your age is :- ", age);


# Note :- Result for input() is always a string in python 

#  Here , age is int but input() will always gives a string
print(type(age)) # ! thus here age will be string 

# To convert into int while taking input() , we have to type cast the input()  function
#  age  = int(input("Enter your age "))


# ! Expression Execution :- 

#! a) String and Numeric values can operate together with * i.e it means string will be multiplied or repeat numeric value times 

A,B = 2,3
Txt = "@";
print(2*Txt*3); 
#  ouptut will be @@@@@@ i.e 6 times

#! b) String and String can operate with * :- two string can be concatinated using +

C,D = "2",3
T = "@"
print((C+T)*D);
#  output will be  2@2@2@


# ! Result of divison operator with two integers will be float 
print(5/6)
print(type(5/5))


#! d) Integer division with float and int will give int displayed as float
print(1.5//3 , 1.5/3)






# ! Realtional operator

#! a) Arithmatic operator =(+ , - , * , / , % ,**)
print(2**3); 
# output :- it means 2 to the power 3 (2^3) ie 8
# The ** operator in Python is used for exponentiation, meaning it raises the left operand to the power of the right operand. i.e, result = base ** exponent

#! b) Relational / Comparision operators (==, != , > , < , >= ,<= )

#! c) Assignment operators ( = , += , -= *= /= %= **=);

#! d) Logical operator (not , or , and )
print(not False)
print(not True)



# ! Type Casting :-
a = int("2")
print(type(a));

b = 3.14;
b = str(b);
print(type(b))

