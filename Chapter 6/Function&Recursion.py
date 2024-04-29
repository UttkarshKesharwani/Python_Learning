
#! Function :- It is block of statement ,which is used to perform specific task 

#! Syntax:-
# def func_name(param1,param2,....): #! function definition 
#   # some work
#   return val 

# func_name(arg1,arg2,...); #! function calling 

#! Printing sum of two number using function 
def cal_sum(a,b):
  # print(a+b)
  return a+b

sum = (cal_sum(5,3))
print(sum)
# cal_sum(5,3)

# ! Note :- function which do not return anything would return none by default

#! Write a function to print the list
cities = ["pune","delhi","banglore","kolkata"];
def print_cities(cities):
  for ele in cities:
    print(ele)

print_cities(cities)


#! Recursion :- when a function call iteself inside a function is known as recursion 
# ! Note :- Go to another tution for brief discussion of recursion 


list = [1,2,3,4,5]
def print_list(list , idx):
  if(idx == len(list)):
    return ;
  print(list[idx]);
  print_list(list,idx+1)

print_list(list,0)
