# <--------------------------STRINGS------------------->


# text="python"
# print(text[0])
# print(text[1])
# print(text[2])
# print(text[3])
# print(text[4])
# print(text[5])
# print(text[-6])
# print(text[-5])
# print(text[-4])
# print(text[-3])
# print(text[-2])
# print(text[-1])
# print(text)


# text="python"
# for i in range(10):
#    print(text)

# text="python"
# print(text[1:3])
# print(text[1:5])
# print(text[0:3])
# print(text[0:5])
# print(text[1:])
# print(text[:5])

# text="python"
# new_text= "j" + text[1:]
# print(new_text)

# text="python"
# print(text[1::-1])

# print(dir(str))

# mobile_number=input("enter your number: ")
# valid_number=mobile_number.isdigit()
# print(valid_number)

# pan_number=input("enter your pan number: ")
# valid_number=pan_number.isalnum()
# print(valid_number)

# pan_number=input("enter your pan number: ")
# valid_number=pan_number.isalnum()
# format_valid_number=pan_number.upper()
# print(valid_number)

# a=1
# while a<30:
#    print(a)   ---------------WHILE LOOP-------------
#    a=a+1

# count = 0
# while count < 5:
#    print(f"Current count: {count}") ---------to print 1 2 3 4 5
#    count += 1

# a="manu"
# for i in range(20):  -------------- to print name in 20 or 30...... etc, times
#    print(a)


# define a list ----------------------lIST--------------

# empty_list=[]
# print(type(empty_list))
# print(empty_list)

# define list with nums

# list=[10,20,30,40,50,]
# print(type(list))
# print(list)

# define list with texts

# list=["apple","banana","orange","mango"]
# print(type(list))
# print(list)

# define list with mixed nums and text

# list_mixed=["apple",30,40,"python",3.14,"orange","html",45,49,65]
# print(list_mixed)


# list inside list

# list=[10,20,30,40,50,["apple","banana","orange","mango"]] 
# print(list)

# using class list

# empty_list=list()
# print(type(empty_list))
# print(empty_list)

# looping in list

# list=[10,20,30,40,50,60,70,80,90,100]
# for i in list:
#    print(list)

# list=[10,20,30,40,50,60,70,80,90,100]
# for i in list:
#    print(i)

# using range

# custom_list=list(range(0,26,5))
# print(custom_list)

# days=("mon","tue","wed","thru","fri","sat","sun")
# day=input("enter  day: ")
# if day in days:
#     print("day exists")
# else:
#     print("The Day not exists")

#------TYPES IN LISTS OPERATIONS------

# list=[10,20,30,40,50,]
# list.pop()
# print(list)

# list=[10,20,30,40,50,]
# list.clear()
# print(list)

# list=[10,20,30,40,50,]
# list.remove(10)
# print(list)

# list=[10,20,30,40,50,] ------POSITON OF THE VALUE
# print(list.index(40))

# list=[10,20,30,40,50,10,20,30,40,50,10,220,30,40,50]
# print(list.index(20,2))
# print(list.index(20,2,8))

# list=[10,20,30,40,50,10,20,30,40,50,10,20,30,40,50]  ------NO OF TIMES VALUES REPEATED
# print(list.count(10))  

# list=[10,20,30,40,50,]
# print(list)
# list.reverse()
# print(list)

# list=[50,30,40,20,10,]
# print(list.sort())
# asc_sort=list.sort()
# print(asc_sort)

#---------------------TUPLES-------------------------

# empty_tuple=()
# print(type(empty_tuple))

#numbers

# tuple=(10,20,30,40,50)
# print((tuple))

#words

# tuple=("java","python","c","HTML","c++")
# print(tuple)

#mixed data

# tuple_mixed=(10,"java",30,"python",40,"cloud")
# print(tuple_mixed)

#list to tuples

# list=[10,20,30,40,50,]
# print(list)

# tuple=tuple(list)
# print(tuple)

#AS IT IS LIST DONE EXAMPLES UP TO LINE "124"

#-----TUPLE OPERATIONS-------

# print(dir(tuple))

#INDEX ------POSITON OF THE VALUE

# tuple=(10,20,30,40,50)
# print(tuple.index(20))

#COUNT ------NO OF TIMES VALUES REPEATED

# tuple=(10,20,30,40,50,10,20,30,40,50,10,20,30,40,50)
# print(tuple.count(20))

#TUPLES PACKING AND UNPACKING

# person=("manu",22,"data analyst") #PACKING
# name,age,course=person #UNPACKING
# print(person)
# print(name)
# print(age)
# print(course)

# t1=([10,20],[30,40],[50,60])
# print(t1)
# print(t1[0][0])

# t1=([10,20],[30,40],[50,60])
# t1[0][0]=100 #-----chaging the list in the tuple not the tuple
# print(t1)


#-----------------------DICTINORIES------------------------

# empty_dict={}
# print(type(empty_dict))
# print(empty_dict)

# list=[]
# tuple=()
# dic={key:value}

#number dict

# dict={1:10,2:20,3:30,4:40,5:50}
# print(dict)
# print(dict[3])

#text

# dict={"course1":"python","course2":"java","course3":"cloud"}
# print(dict)
# print(dict["course1"])

#Mixed data

# dict={1:10,2:20,"course1":"python","course2":"java"}
# print(dict)
# print(dict[2])
# print(dict["course1"])

#Dict inside dict

# students={101:{"name":"manu","age":22},
#           102:{"name":"kedar","age":22}}
# print(students)
# print(students[101])

#Update data ->methods

# fruits={"a":"apple","b":"mango","c":"banana"}
# print(fruits)
# fruits["c"]="cherry" #------use assingment
# print(fruits)

#------DICT OPERATIONS--------

# print(dir(dict))

#UPDATE ->update the key value

# fruits={"a":"apple","b":"mango","c":"banana"}
# print(fruits)

# fruits["c"]="cherry" #------use assingment
# print(fruits)

# fruits["a"]="berry" #------use assingment
# print(fruits)

#POP -> Remove items with specified kyes

# fruits={"a":"apple","b":"mango","c":"banana"}
# fruits.pop("c")
# print(fruits)

#POPITEM -> Remove the last insert item

# fruits={"a":"apple","b":"mango","c":"banana"}
# print(fruits)
# fruits.pop("c")
# print(fruits)
# fruits.popitem()
# print(fruits)

#Clear -> Clear the all items

# fruits={"a":"apple","b":"mango","c":"banana"}
# print(fruits)
# fruits.clear()
# print(fruits)

#ACCESS REALATED METHODS

# Get() -> get the value for the key 

# dict={1:10,2:20,3:30,4:40,5:50}
# print(dict)
# print(dict[3])

# print(dict.get(2))
# print(dict.get(0))

# keys() -> returns all the keys only

# dict={1:10,2:20,3:30,4:40,5:50}
# print(dict.keys())

# dict={1:10,2:20,3:30,4:40,5:50}
# only_keys=dict.keys()
# for i in  only_keys:
#     print(i)

# Values() -> returns all the values

# dict={1:10,2:20,3:30,4:40,5:50}
# print(dict.values())

# only_values=dict.values()
# for i in only_values:
#     print(i)

# items() -> returns all the keys and values

# dict={1:10,2:20,3:30,4:40,5:50}
# print(dict.items())

#Setdefault -> returns value of a key,if it not present in set 

# dict={1:10,2:20,3:30,4:40,5:50}
# print(dict) 
# dict.setdefault(6,60)
# print(dict)

# -------------------------------------SETS-------------------------------------------

# empty_set={}
# print(empty_set)
# print(type(empty_set))

#use set claSS

# empty_set=set()
# print(empty_set)
# print(type(empty_set))

#set numbers

# set_nums={10,20,30,40,50}
# print(set_nums) #------------->UNORDERED

# set_nums={10,20,30,40,50,10,20,30} #------------->duplicate values
# print(set_nums) #----------------->donot print duplicate values

#text data

# set_nums={"cloud","python","java"}
# print(set_nums)

#mixed data

# set_nums={10,20,30,40,50,"cloud","python","java"}
# print(set_nums)

#OPERATIONS / METHODS IN SETS

#add()-------->add an element to set
# s1={1,2,3,4,5}
# s1.add(6)
# print(s1)

#update()------->add multiple elements from itreble only
# s1={10,20,30,40,50}
# # s1.update(60)---->'int' object is not iterable
# s1.update([60,70]) #---->list 
# print(s1)
# s1.update((90,100,110)) #---->using tuple 
# print(s1)
# s1.update([120,130,150],[160,170,180]) #------>accesing multiple
# print(s1)

#Remove()--------->remove a specific element,raise error if not found
# s1={10,20,30,40,50}
# s1.remove(20)
# print(s1)

#Discard()-------->remove a specific element,raise NOerror if not found
# s1={10,20,30,40,50}
# # s1.discard(60)------>it shows no error
# s1.discard(20)
# print(s1)

#clear()---------->remove all elements
# s1={10,20,30,40,50}
# s1.clear()
# print(s1)

#pop()------------>removes random elements
# s1={10,20,30,40,50}
# s1.pop()
# print(s1)

#set specific operations
s1={10,20,30,40,50}
s2={40,50,80,90,100}

#union()----------->combine elements from both sets
print(s1.union(s2))
print(s1 | s2) #---->using symbol

#intersection()------->extract only common elements
print(s1.intersection(s2))
print(s1 & s2) #-------symbol

#intersection_update()---------->extract only common elements ,updates the calling set
print(s1)
print(s2)
print(s1.intersection_update(s2))
print(s1)
print(s2)

#difference()--------->remove the elements which also occur in the other set
print(s1)
print(s2)
print(s1.difference(s2))
print(s1)
print(s2)

#difference_update()-------->remove the elements which also occur in the other set,update calling set
#symmetric_defference() "symbol- ^"--------->remove common elements and take combine elements left in both sets
#symmetric_defference_update()--------->remove common elements and take combine elements left in both sets,update calling cell
#issubset----------->checks if given set subset to another set
#issuperset--------->checks if given set superset to another set
#isdisjoint--------->check if 2 sets have no common elements
#copy------------>create a shallow copy