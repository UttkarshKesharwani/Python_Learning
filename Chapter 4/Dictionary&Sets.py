
#! Dictionary in pyhon :- Dictonaries are used to store data values in key:value pairs
# ! They are unordered , mutable and don't allow duplicate keys

info ={
  "name":"Uttkarsh",
  "class":12,
  "age":20,
  "subjects":{
    "phy":28,
    "chem":29,
    "math":30
  },
  18:True,
 }
print(info)
print(info["subjects"]["phy"])
print(info.get("name"))
print(type(info["class"]))

info["surname"]="kesharwani" #! assigining key:value pairs in dictionary 

print(info)


#! Some important "Dictonary Methods"

print(info.keys()) #! returns all keys in a list 
print(list(info.keys())) 

print(info.values()) #! returns all values
print(list(info.values())) 

print(info.items()) #! returns all (key:value) pairs as tuples in a list
print(list(info.items())) #! returns all (key:value) pairs as tuples in a list

print(info.get("name")) #! returns the value according to key

new_info={"city":"delhi"}
info.update(new_info) #! returns the key according to value
print(info)

  

#! Set in Python :- Set is the collection of the unordered items . Each element in the set must be unique and immutable i.e set is mutable but value of set is immutable . it doesnt support indexing or slicing 

set1= { 1,4,8,(1,34,8),3,2,2,1,1,4,2,1,"uttkarsh"}

print(set1) #! duplicate item is not allowed
print(type(set1))

#! Some builtin "Set Functions"


set2= set()
set2.add(1) #! adds an element 
set2.add(7)  
set2.add((1,2,3,4)) 

set2.remove(1)#! removes the elements from the set

print(set2.pop()) #! removes a random value and return 
print(set2)

set2.clear() #! empties the set 


set_union1 = {1,2,3}
set_union2 = {3,4,5}

print(set_union1.union(set_union2)) #! union fun will make union of two sets and return new set

print(set_union1.intersection(set_union2)) #! intersection fun will make intersection of two sets and return new set 



